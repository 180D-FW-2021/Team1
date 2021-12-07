## Credits

The BerryIMU code which gathers the sensor information is adapted from http://github.com/ozzmaker/BerryIMU.git.

## Information and Statistics

This code gathers a bunch of data from the BerryIMU sensors, sets arbitrary thresholds to detect when certain gestures are executed, and sends MQTT messages to our server with which gesture was detected. There are various flags to detect when a gesture was just made so as to prevent the detection of its opposite gesture within a certain time frame, as many gestures require the Pi to be put back in its original position after. 

Currently, the gesture accuracy is as follows:

Power off: 35%

Power on: 95%

Volume down: 60%

Volume up: 60%

Channel down: 85%

Channel up: 90%

More statistics can be found in `gesture_data_report.pdf` in this directory. Raw testing data can be found within `gesture_data.zip`.

Recognition of power off in particular is buggy due to it continually recognizing the gesture as power on due to needing to lift the Pi first in order to flick it down. However, since power on/off are actually the same MQTT command "power," this may not actually matter. I will review this more next quarter.

Volume up/down both are buggy in that they often register as one another instead of themselves. The reason for this may be the degree to which I angle the Pi while attempting to get the gesture to register. Perhaps lowering the threshold will help.

Channel down/up appear to work well, but more testing will be done to see if I can get accuracy above 95%.

## In the main directory, IMUpi.py is the actual file to run in order to use the files within this directory. None of these files should be executed directly.
