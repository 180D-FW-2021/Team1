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
Graphical user interface created with TKinter to help the user orient themselves with the product.

Directory: `gui`
