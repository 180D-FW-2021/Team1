This code gathers a bunch of data from the BerryIMU sensors, sets arbitrary thresholds to detect when certain gestures are executed, and sends MQTT messages to our server with which gesture was detected. There are various flags to detect when a gesture was just made so as to prevent the detection of its opposite gesture within a certain time frame, as many gestures require the Pi to be put back in its original position after. 

Currently, the gesture accuracy is as follows:

Power off: 35%

Power on: 95%

Volume down: 60%

Volume up: 60%

Channel down: 85%

Channel up: 90%

Power off in particular is buggy due to the need to raise the Pi beforehand in order to flick it back down. In order to fix this, next quarter I will be attempting to add in a "flicked_up" flag which will attempt to wait for a "flicked_down" flag to determine power off. If no flicked_down flag is found, then it will power on as normal.

Volume up/down both are buggy in that they often register as one another instead of themselves. The reason for this is the degree to which I angle the Pi while attempting to get the gesture to register. Perhaps lowering the threshold will help.

Channel down/up appear to work well, but more testing will be done to see if I can get accuracy above 95%.

In the main directory, IMUpi.py is the actual file to run in order to use the files within this directory. None of these files should be executed directly.

The BerryIMU code which gathers the sensor information is adapted from http://github.com/ozzmaker/BerryIMU.git.
