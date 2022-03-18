## Credits

Isaac Xu's responsibility

## Contents

check_dab.py
  - demo code for detecting if a person is in a dab position

check_psy.py
  - demo code for detecting if both arms are at a 90 degree angle
 
check_three_pose.py
  - demo code for detecting three poses: T-pose, tree pose, and Warrior II pose
  
gui_pose_test.py
  - demo code for combining gui and posture detection code
  
hands_together.py
  - demo code for detecting if a person has their hands in close contact
  
jump_stand.py
  - demo code for detecting if a person is either jumping, crouching, or standing
  
left_right.py
  - demo code for detecting if a person is on the right side, left side, or center of the webcam
  
poses.txt
  - current list of poses and how to achieve them
  
together.py
  - posture detection code that detects a right or left dab, arms at 90 degrees, hands placed together, a T-pose, and both arms straight and legs at 90 degrees
  - sends it to poses.py in the main folder so that the command corresponding to the pose is executed
  - requires one available webcam on the computer

Pose Detect.mp4
  - posture detection code in action, showing that dabs change the volume, and a hands-together and T-pose "presses" the power button
  - having both arms at 90 degree angle, or having both arms straight while legs are at a 90 degree angle would change the channel up and down, but that T.V didn't have any channels to change. The signal was still sent to the mqtt.

Pose Detection Trials.mkv
  - all the trials done to detect if there was any errors when detecting poses 

Pose_Demonstration.mp4
  - a demonstration of how to properly use the pose detection to control the AirController

dependencies.txt
  - a list of all the dependencies Isaac's virtual environment uses to run pose detection code

pose_install_script.sh
  - make sure to run this, since it contains the modules that are required to run both pose detection and speech detection code

testing.py
  - testing code that won't interfere with the main approved detection

required installs.txt
  - a list of the required installs (besides those already in Anaconda) needed to run only pose detection code

## Code tags
  Where Isaac got help for the code from
  - https://bleedai.com/introduction-to-pose-detection-2/
  - https://bleedai.com/introduction-to-pose-detection-and-basic-pose-classification/

## Known Bugs

## Improvements
- organize list of dependencies (current list is 300 above dependencies)

## Decisions Made
- this was the default
- current list of poses used because they are easily identifiable and easily done by majority of people, but might have to change in the future
- 6 poses used: two for power, two for channel, two for volume
