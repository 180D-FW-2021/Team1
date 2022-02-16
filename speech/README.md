## Credits

This part of the project was Steven's responsibility.

Contains `speech_processing.py`, which implements the speech processing module of this project. Transcribes all audio to text, and detects keywords "power", "channel", and "volume".

Code adapted from Google Cloud Speech-to-Text API example code:
https://cloud.google.com/speech-to-text/docs/samples?hl=en_US

In order to run this code, please run the following commands:
```
pip install --upgrade google-cloud-speech
brew install portaudio
pip install pyaudio
```

Also required to run this code is a Google Cloud private key. It has been removed from this public repository, but is available upon request.
After obtaining the key, append `export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"` to your ~/.bash_profile file, replacing "KEY_PATH" with the path to the private key on your local machine, and restart your shell.

Future Improvements:
* Support channel and volume jumps of more than one increment
* Support additional commands (e.g. change input)
