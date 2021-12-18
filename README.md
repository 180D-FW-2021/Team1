# AirController

Being forced to get up and get the remote to just change the volume is a hassle for households that use a TV. To fix this very serious issue we have decided to prototype AirController, a system that can take in hand gestures as inputs and accordingly modify the volume. In this case, the user can make a specific gesture using their hand/arm in order to utilize a specific control option on the TV. This way those who are disabled or are not within reach of a remote can use their hands to access controls.

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
Download all the files contained within our repo onto two Raspberry Pis and a computer with a webcam. 

Run IMUpi.py on one Raspberry Pi which is hooked up to a BerryIMU.

Run mainPi.py on another Raspberry Pi which is hooked up to an IR emitter set up next to a TV's IR receiver. Requires LIRC to be installed, along with some TV remote configuation files

Run gui.py (contained within the `gui` directory) on a computer with both a webcam and microphone. 

The two Raspberry Pis will communicate with each other. The computer will communicate with the Raspi running mainPi.py. The Raspi running mainPi.py will then communicate with the TV to actually be able to implement our remote. The user will be able to use gesture commands on the Raspi running IMUpi.py, or webcam-based/voice-based commands on the computer. The computer's GUI will also provide a tutorial of how to use the Raspi gesture system, as well as serve as the way for the user to launch the webcam and voice modules. The voice module has some further requirements currently with getting a key from Google to be able to use it.

## Controls

Pose (Webcam) - current poses include a right dab (volume up), left dab (volume down), both arms at a 90 degree angle (channel up), both hands together (power), both arms straight and body straight (power), and both arms straight and both legs at a 90 degree angle (channel down). The webcam must properly recognize the user first for it to start working. 
Note: when the camera freezes for a bit, that's ok, since the code is made such that the program sleeps for 1 - 5 seconds before trying to recognize another pose, so that there won't be an overflow error.
For more detail in pose detection, look through the poses.txt file in pose_detection_code folder.

Speech - 

Gesture (BerryIMU) - possible gestures include tilt right (volume up), tilt left (volume down), flick right (channel up), flick left (channel down), flick up (power on), and flick down (power off). The BerryIMU should be facing forward and parallel to the ground as its neutral position. For a visual explanation, launch gui.py and view the tutorial videos.

## Credits

Developed by Steven Chu, Maksym Prokopovych, Sierra Rose, and Isaac Xu.

IMUpi.py: this file, and others in the `gesture` directory, are adapted from http://github.com/ozzmaker/BerryIMU.git. 

mainPi.py: this file, and others in the `comms` directory, are adapted from lab 3.

pose.py: this file, and others in the `pose_detection_code` directory, are adapted from lab 1 as well as various online sources, which are further referenced in the README of the `pose_detection_code` directory. Also adapted from https://bleedai.com/, specifically https://bleedai.com/introduction-to-pose-detection-2/ and https://bleedai.com/introduction-to-pose-detection-and-basic-pose-classification/

speech_processing.py: this file, and others in the `speech` directory, are adapted from lab 4.

Further credits can be found in the READMEs of each directory.
