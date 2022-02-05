## Credits

Isaac Xu's responsibility

## Contents

check_dab.py
  - posture detection code for a dab

check_psy.py
  - posture detection code for both arms at a 90 degree angle
 
check_three_pose.py
  - posture detection code for three poses: T-pose, tree pose, and Warrior II pose
  
gui_pose_test.py
  - demo code for combining gui and posture detection code
  
hands_together.py
  - posture detection code for having both hands together
  
jump_stand.py
  - demo code for detecting if a person is either jumping, crouching, or standing
  
left_right.py
  - demo code for detecting if a person is on the right side, left side, or center of the webcam
  
poses.txt
  - current list of poses and how to achieve them
  
together.py
  - posture detection code that detects a right or left dab, arms at 90 degrees, hands placed together, a T-pose, and both arms straight and legs at 90 degrees
  - sends it to poses.py in the main folder so that the command corresponding to the pose is executed
  - CURRENT: does not generate a webcam that lets the user see what pose is being identified/the webcam view

Pose Detect.mp4
  - posture detection code in action, showing that dabs change the volume, and a hands-together and T-pose "presses" the power button
  - having both arms at 90 degree angle, or having both arms straight while legs are at a 90 degree angle would change the channel up and down, but that T.V didn't have any channels to change. The signal was still sent to the mqtt.

pose_detection trials.mkv
  - all the trials done to detect if there was any errors when detecting poses 

dependencies.txt
  - a list of all the dependencies Isaac's virtual environment uses to run pose detection code

pose_install_script.sh
  - make sure to run this, since it contains the modules that are required to run pose detection code

## Code tags
  Where Isaac got the code from 
  - https://bleedai.com/introduction-to-pose-detection-2/
  - https://bleedai.com/introduction-to-pose-detection-and-basic-pose-classification/

## Known Bugs
- sometimes together.py detects the wrong pose, or may sometimes not identify a person within view

## Improvements
- organize list of dependencies (current list is 300 above dependencies)

## Decisions Made
- use OpenCV, Mediapipe because others (openpose, blazepose) weren't able to be ran
- this was the default
- current list of poses used because they are easily identifiable and easily done by majority of people
