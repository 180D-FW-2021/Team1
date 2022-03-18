# AirController

Being forced to get up and get the remote to just change the volume is a hassle for households that use a TV. To fix this issue, we have decided to prototype AirController, a system that can take in hand gestures as inputs and accordingly modify the volume. In this case, the user can make a specific gesture using their hand/arm in order to utilize a specific control option on the TV. This way those who are disabled or are not within reach of a remote can use their hands to access controls.

## Pose Recognition (OpenCV and MediaPipe)
Uses computer vision and image processing to detect specific body positions and poses. Uses MQTT to communicate detected poses to the subscriber Raspberry Pi.

Folder: sample_poses show images of sample poses that are to be detected from the AirController.

Directory: `pose_detection_code`

## Speech Recognition
Uses Google Cloud Speech-to-Text to detect keywords for specific voice commands.  Uses MQTT to communicate detected commands to the subscriber Raspberry Pi.

Directory: `speech`

## Gesture Recognition
Uses a programmed BerryIMU to detect specific hand motions. Uses MQTT to communicate detected gestures to the subscriber Raspberry Pi.

Directory: `gesture`

## GUI
Graphical user interface created with TKinter to help the user orient themselves with the product. Includes video tutorials of how to use the product. Launches the speech recognition and pose recognition modules on the user's computer.

Directory: `gui`

## Communications
Communication interface for the two Raspberry Pis and laptop to talk to one another and the TV. Uses MQTT publisher/subscriber model. Requires paho-mqtt Python library.

Directory: `comms`

## Demonstration
Demonstrations of our individual subcomponents of our projects working.

Directory: `demonstration_videos`

## Download & Set-Up
Please follow the user manual for detailed instructions on how to set up the AirController.

## Controls

Pose (Webcam) - current poses include a right dab (volume up), left dab (volume down), both arms at a 90 degree angle (channel up), both hands together (power), both arms straight and body straight (power), and both arms straight and both legs at a 90 degree angle (channel down). The webcam must properly recognize the user first for it to start working. 

Speech - currently supports keyword detection for "volume", "channel", and "power". To adjust volume, say any combination of "volume" and "up/down". To adjust channel, say any combination of "channel" and "up/down". To turn the TV on or off, say any combination of "power" and "on/off".

Gesture (BerryIMU) - possible gestures include tilt right (volume up), tilt left (volume down), flick right (channel up), flick left (channel down), flick up (power on), and flick down (power off). The BerryIMU should be facing forward and parallel to the ground as its neutral position. For a visual explanation, launch gui.py and view the tutorial videos.

## Requirements

Make sure to download all the required modules from requirements.txt by running
pip install -r requirements.txt

## Credits

Developed by Steven Chu, Maksym Prokopovych, Sierra Rose, and Isaac Xu.

IMUpi.py: this file, and others in the `gesture` directory, are adapted from http://github.com/ozzmaker/BerryIMU.git. 

mainPi.py: this file, and others in the `comms` directory, are adapted from lab 3. Configuring LIRC adapted from https://www.hackster.io/austin-stanton/creating-a-raspberry-pi-universal-remote-with-lirc-2fd581

pose.py: this file, and others in the `pose_detection_code` directory, are adapted from lab 1 as well as various online sources, which are further referenced in the README of the `pose_detection_code` directory. Also adapted from https://bleedai.com/, specifically https://bleedai.com/introduction-to-pose-detection-2/ and https://bleedai.com/introduction-to-pose-detection-and-basic-pose-classification/

speech_processing.py: this file, and others in the `speech` directory, are adapted from example code provided by Google Cloud documentation.
https://cloud.google.com/speech-to-text/docs/samples?hl=en_US

Further credits can be found in the READMEs of each directory.
