## Credits

All of the code in this directory which gathers sensor information from the BerryIMU is adapted from http://github.com/ozzmaker/BerryIMU.git.

This portion of the project was Sierra's responsibility.

## Information and Statistics

This code gathers a bunch of data from the BerryIMU sensors, sets arbitrary thresholds to detect when certain gestures are executed, and sends MQTT messages to our server with which gesture was detected. There are various flags to detect when a gesture was just made so as to prevent the detection of its opposite gesture within a certain time frame, as many gestures require the Pi to be put back in its original position after. 

Currently, the gesture accuracy is as follows:

Power off: 93%

Power on: 100%

Volume down: 100%

Volume up: 100%

Channel down: 100%

Channel up: 100%

Fall detection: 81%

More statistics can be found in the `gesture_data` directory. The latest data is within `winter_data_final`.

I first made the decision to use the accXangle when detecting volume up/down because it was the value that changed the most while making the gesture and just reading the raw data of the BerryIMU. However, it is somewhat unreliable due in part to its noisiness, and so I will be reviewing my choice of variable next quarter.

I also then made the choice to use faux derivatives in creating difference_gyro_X/difference_gyro_Z to use for detecting "flicking" motions (channel up/down, power on/off). This is because they are much easier than actually deriving anything in Python, and because they serve the same purpose: to see the change over time within a certain reading. By making these faux derivatives of the gyro_X and gyro_Z readings of the BerryIMU, I was able to detect when the user rapidly flicked their IMU in a given direction to be able to detect these gestures.

Similarly, I also created difference_gyro_Y, which is solely used to detect when the Pi is falling. Fall detection has about 81% accuracy in detecting a fall (only tested without the case due to movement constraints with the shorter wire). While detecting falls is important, perhaps more important is not ignoring a user's input, thus causing the fall detection to not be perhaps as sensitive as it could be to get 95%+ accuracy. However, this enables the user to not have their inputs ignored, which is definitively more important than successfully detecting a fall to block excess inputs. Thus, while improvements may be possible, we are satisfied with where the fall detection currently is.

## In the main directory, IMUpi.py is the actual file to run in order to use the files within this directory. None of these files should be executed directly.

