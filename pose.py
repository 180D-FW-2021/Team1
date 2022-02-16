import mediapipe as mp
import comms.comms as comms
from pose_detection_code.together import *
import time

server = "test.mosquitto.org"

conn = comms.mqttCommunicator(server, {})

#conn.send_command("volumeUp")

# Initializing mediapipe pose class.
#mp_pose = mp.solutions.pose
 
# Setting up the Pose function.
#pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.3, model_complexity=2)
 
# Initializing mediapipe drawing class, useful for annotation.
#mp_drawing = mp.solutions.drawing_utils

#setup pose function for video#
#pose_video = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=1)


# Initialize the VideoCapture object to read from the webcam.
camera_video = cv2.VideoCapture(0)

# Initialize a resizable window.
cv2.namedWindow('All Together Pose', cv2.WINDOW_NORMAL)
 
# Iterate until the webcam is accessed successfully.
while camera_video.isOpened():
    
    # Read a frame.
    ok, frame = camera_video.read()
    
    # Check if frame is not read properly.
    if not ok:
        
        # Continue to the next iteration to read the next frame and ignore the empty camera frame.
        continue
    
    # Flip the frame horizontally for natural (selfie-view) visualization.
    frame = cv2.flip(frame, 1)
    
    # Get the width and height of the frame
    frame_height, frame_width, _ =  frame.shape
    
    # Resize the frame while keeping the aspect ratio.
    frame = cv2.resize(frame, (int(frame_width * (640 / frame_height)), 640))
    
    
    # Perform Pose landmark detection.
    frame, landmarks = detectPose(frame, pose_video, draw=True, display=False)
    
    curr_pose = 'Unknown Pose'
    
    # Check if the landmarks are detected.
    if landmarks:
        
        # Perform the Pose Classification.
        frame, curr_pose = checkpose(landmarks, frame, display=False)
    
    if curr_pose == 'right dab':
        conn.send_command("volumeUp")
        time.sleep(1)
    elif curr_pose == 'left dab':
        conn.send_command("volumeDown")
        time.sleep(1)
    elif curr_pose == 'sumo':
        conn.send_command("channelDown")
        time.sleep(1)
    elif curr_pose == 'psy pose':
        conn.send_command("channelUp")
        time.sleep(1)
    elif curr_pose == 'hands together' or curr_pose == 'T-pose':
        conn.send_command("power")
        time.sleep(5)


    #if a dab has been detected, record that time
    #then if another dab is detected, compare that with the previous time
    #and depending on that do stuff
    #use a flag

    # Display the frame.
    cv2.imshow('Pose Classification', frame)
    
    # Wait until a key is pressed.
    # Retreive the ASCII code of the key pressed
    k = cv2.waitKey(1) & 0xFF
    
    # Check if 'ESC' is pressed.
    if(k == 27):
        
        # Break the loop.
        break
 
# Release the VideoCapture object and close the windows.
camera_video.release()
