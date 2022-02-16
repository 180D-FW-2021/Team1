from __future__ import division

import re
import sys
import comms.comms as comms

from google.cloud import speech

import pyaudio
from six.moves import queue

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

server = "test.mosquitto.org"
connection = comms.mqttCommunicator(server, {})

class MicrophoneStream(object):
    """Opens a recording stream as a generator yielding the audio chunks."""

    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk

        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            # The API currently only supports 1-channel (mono) audio
            # https://goo.gl/z757pE
            channels=1,
            rate=self._rate,
            input=True,
            frames_per_buffer=self._chunk,
            # Run the audio stream asynchronously to fill the buffer object.
            # This is necessary so that the input device's buffer doesn't
            # overflow while the calling thread makes network requests, etc.
            stream_callback=self._fill_buffer,
        )

        self.closed = False

        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            # Now consume whatever other data's still buffered.
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b"".join(data)


def listen_print_loop(responses):
    """Iterates through server responses and prints them.
    The responses passed is a generator that will block until a response
    is provided by the server.
    Each response may contain multiple results, and each result may contain
    multiple alternatives; for details, see https://goo.gl/tjCPAU.  Here we
    print only the transcription for the top alternative of the top result.
    In this case, responses are provided for interim results as well. If the
    response is an interim one, print a line feed at the end of it, to allow
    the next result to overwrite it, until the response is a final one. For the
    final one, print a newline to preserve the finalized transcription.
    """
    num_chars_printed = 0
    for response in responses:
        if not response.results:
            continue

        # The `results` list is consecutive. For streaming, we only care about
        # the first result being considered, since once it's `is_final`, it
        # moves on to considering the next utterance.
        result = response.results[0]
        if not result.alternatives:
            continue

        # Display the transcription of the top alternative.
        transcript = result.alternatives[0].transcript

        # Display interim results, but with a carriage return at the end of the
        # line, so subsequent lines will overwrite them.
        #
        # If the previous result was longer than this one, we need to print
        # some extra spaces to overwrite the previous result
        overwrite_chars = " " * (num_chars_printed - len(transcript))

        if not result.is_final:
            sys.stdout.write(transcript + overwrite_chars + "\r")
            sys.stdout.flush()

            num_chars_printed = len(transcript)

        else:
            print(transcript + overwrite_chars)

            # workaround because certain numbers show up in word form with
            # speech-to-text
            single_num_digit_map = {
                    'zero':'0',
                    'one':'1',
                    'two':'2',
                    'three':'3',
                    'four':'4',
                    'five':'5',
                    'six':'6',
                    'seven':'7',
                    'eight':'8',
                    'nine':'9',
                    'ten':'10'
            }
            
            # volume command detection
            if re.search(r"\b(volume)\b", transcript, re.I):
                # regular expression detects numbers 0-100
                volume = re.search("[^\d](\d{1,2}|100)%?$", transcript, re.I)
                # detect word form numbers zero-ten
                single_digit_volume = re.search(r"\b(zero|one|two|three|four|five|six|seven|eight|nine|ten)\b", transcript, re.I)
                # increase or decrease volume by 1
                step_volume = re.search(r"\b(up|down)\b", transcript, re.I)
                if volume:
                    print("COMMAND DETECTED - Setting volume to" + volume.group(0))  
                elif single_digit_volume:
                    print("COMMAND DETECTED - Setting volume to " + single_num_digit_map[single_digit_volume.group(0).lower()])

                elif step_volume:
                    step = step_volume.group(0)
                    if step == "up":
                        connection.send_command("volumeUp")
                    else:
                        connection.send_command("volumeDown")
                    print("COMMAND DETECTED - Volume " + step)

                else:
                    print("COMMAND ERROR - No valid change detected")

            # channel command detection
            elif re.search(r"\b(channel)\b", transcript, re.I):
                # regular expression detects any three-digit number
                channel = re.search("([^\d]\d{1,3})%?$", transcript, re.I)
                # detect word form numbers zero-ten
                single_digit_channel = re.search(r"\b(zero|one|two|three|four|five|six|seven|eight|nine|ten)\b", transcript, re.I)
                # increase or decrease channel by 1
                step_channel = re.search(r"\b(up|down)\b", transcript, re.I)
                if channel:
                    print("COMMAND DETECTED - Setting channel to" + channel.group(0))
                elif single_digit_channel:
                    print("COMMAND DETECTED - Setting channel to " + single_num_digit_map[single_digit_channel.group(0).lower()])

                elif step_channel:
                    step = step_channel.group(0)
                    if step == "up":
                        connection.send_command("channelUp")
                    else:
                        connection.send_command("channelDown")
                    print("COMMAND DETECTED - Channel " + step_channel.group(0))
                else:
                    print("COMMAND ERROR - No valid change detected")
            
            # power command detection
            elif re.search(r"\b(power)\b", transcript, re.I):
                # detect on or off option
                power = re.search(r"\b(off|on)\b", transcript, re.I)
                if power:
                    connection.send_command("power")
                    print("COMMAND DETECTED - Powering " + power.group(0))
                else:
                    print("COMMAND ERROR - on/off not specified")

            # change mode command detection
            elif re.search(r"\b(mode)\b", transcript, re.I):
                # detect gesture or pose option
                mode = re.search(r"\b(gesture|pose)\b", transcript, re.I)
                if mode:
                    print("COMMAND DETECTED - Switching to " + mode.group(0) + " mode")
                else:
                    print("COMMAND ERROR - gesture/pose not specified")

            num_chars_printed = 0


def main():
    language_code = "en-US"  # a BCP-47 language tag

    client = speech.SpeechClient()
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code,
    )

    streaming_config = speech.StreamingRecognitionConfig(
        config=config, interim_results=True
    )

    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        requests = (
            speech.StreamingRecognizeRequest(audio_content=content)
            for content in audio_generator
        )

        responses = client.streaming_recognize(streaming_config, requests)

        # Now, put the transcription responses to use.
        listen_print_loop(responses)


if __name__ == "__main__":
    main()
