# AirController

Being forced to get up and get the remote to just change the volume is a hassle for households that use a TV. To fix this very serious issue we have decided to prototype AirController, a system that can take in hand gestures as inputs and accordingly modify the volume. In this case, the user can make a specific gesture using their hand/arm in order to utilize a specific control option on the TV. This way those who are disabled or are not within reach of a remote can use their hands to access controls.

## Gesture Recognition
Uses a programmed BerryIMU to detect specific hand motions and MQTT to communicate detected gestures to the main computer.

Directory: `gesture`

## Pose Recognition
Uses computer vision and image processing to detect specific body positions and poses.

Directory: `pose_detection_code`

## Speech Recognition
Uses Google Cloud Speech-to-Text to detect keywords for specific voice commands.

Directory: `speech`

## GUI
Graphical user interface created with TKinter to help the user orient themselves with the product. Includes video tutorials of how to use the product.

Directory: `gui`

## How to Use
Download all the files contained within our repo onto two Raspberry Pis and a computer with a webcam. Then, run IMUpi.py on one Raspberry Pi. Run mainPi.py on another Raspberry Pi. Run gui.py on the computer. The two Raspberry Pis will communicate with each other. The computer will communicate with the Raspi running mainPi.py. The Raspi running mainPi.py will then communicate with the TV to actually be able to implement our remote. The user will be able to use gesture commands on the Raspi running IMUpi.py, or webcam-based commands on the computer. The computer's GUI will also provide a tutorial of how to use the Raspi gesture system.
