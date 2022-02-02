#test how the pose_detection can work with multiple poses
#determine what our order of priority of poses is like
#the poses we'll use is dab and hands together
#combine both types, i.e the list and the pure thing?
#think about it later

from time import time
from math import hypot

import cv2
import math
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt


# server = "mqtt.eclipseprojects.io"

# conn = comms.mqttCommunicator(server, {})

# #conn.send_command("volumeUp")

# # Initializing mediapipe pose class.
mp_pose = mp.solutions.pose
 
# # Setting up the Pose function.
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.3, model_complexity=2)
 
# # Initializing mediapipe drawing class, useful for annotation.
mp_drawing = mp.solutions.drawing_utils

# #setup pose function for video
pose_video = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=1)

def detectPose(image, pose, draw=False, display=True):
    '''
    This function performs pose detection on an image
    Args:  
        image: The input image with a prominent person whose pose landmarks needs to be detected.
        pose: The pose setup function required to perform the pose detection.
        draw: a boolean value that if set to true the funciton draw pose landmakrs on the output image
        display: a boolean value that is if set to true the function displays the original input image, and
                    the resultant image and returns nothing
    Returns:
        output_image: the input image with the detect pose landmarks drawn if it was specified
        results: the output of the pose landmarks detection on the input image
    '''

    #create a copy of the input image
    output_image = image.copy()

    #convert the image from BGR into RGB format
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    #perform pose detection
    results = pose.process(imageRGB)

    #retrieve the height and width of the input image
    height, width, _ = image.shape

    #initialize a list to store the detected landmarks
    landmarks = []

    #check if any landmarks are detected
    if results.pose_landmarks:

        #iterate over the detected landmarks
        for landmark in results.pose_landmarks.landmark:

            #append the landmark into the list
            #it has already done the modification that multiplies it by the height and width of the image
            landmarks.append((int(landmark.x * width), int(landmark.y * height)))

        #check if the landmarks are specified to be drawn
        if draw:
            #draw pose landmarks on the output image
            mp_drawing.draw_landmarks(image=output_image, landmark_list=results.pose_landmarks,
                                    connections=mp_pose.POSE_CONNECTIONS,
                                    landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255,255,255),
                                                                                thickness=3, circle_radius=3),
                                    connection_drawing_spec=mp_drawing.DrawingSpec(color=(49,125,237),
                                                                                thickness=2, circle_radius=2))

    # Check if the original input image and the resultant image are specified to be displayed.
    if display:
    
        # Display the original input image and the resultant image.
        plt.figure(figsize=[22,22])
        plt.subplot(121);plt.imshow(image[:,:,::-1]);plt.title("Original Image");plt.axis('off');
        plt.subplot(122);plt.imshow(output_image[:,:,::-1]);plt.title("Output Image");plt.axis('off');

    #otherwise
    else:
            
        #return the output image and the found landmarks
        return output_image, landmarks

def calculateAngle(landmark1, landmark2, landmark3):
    '''
    This function calculates angle between three different landmarks.
    Args:
        landmark1: The first landmark containing the x,y and z coordinates.
        landmark2: The second landmark containing the x,y and z coordinates.
        landmark3: The third landmark containing the x,y and z coordinates.
    Returns:
        angle: The calculated angle between the three landmarks.
 
    '''
 
    # Get the required landmarks coordinates.
    x1, y1 = landmark1
    x2, y2= landmark2
    x3, y3 = landmark3
 
    # Calculate the angle between the three points
    angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
    
    # Check if the angle is less than zero.
    if angle < 0:
 
        # Add 360 to the found angle.
        angle += 360
    
    # Return the calculated angle.
    return angle

def checkpose(landmarks, output_image, display=False):
    '''
    This function classifies the pose of the person depending on body angles and distance differences
    There will be a hierarchy of poses, i.e what pose to detect first
    Args:
        landmarks: a list of detected landmarks of the person whose pose needs to be detected
        output_image: a image of the person with the detected pose landmarks drawn
        display: a boolean value that is if set to true the function displays the resultant image with the pose label
        written on it and returns nothing
    Returns:
        output_image: the image with the detected pose landmarks drawn and pose label written
        label: the classified pose label of the person in the output_image
    '''
    #first demo it for two poses: check dab and psy style pose
    #psy requires angle measure of the left and right arms
    #check dab requires euclidean distance between left and right arms, and
    #distance between nose and either elbow

    #initialize the label of the pose, which is unknown at this stage
    label = 'Unknown Pose'

    #specify the color (red) which is used for unknown pose
    color = (0,0,255)

    #here we will calculate the required angles

    #calculate angles required for psy pose
    #for a psy pose we need both arm angles to be at 90 degrees
    left_elbow_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value], landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value], landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value])
    right_elbow_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value], landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value], landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value])

    #here we will calculate the distance between two landmarks

    #calculate euclidean distances required for dab pose
    #the dab pose needs the nose to be close to the elbow
    #and there be a sizeable distance between both hands
    nose_landmark = landmarks[mp_pose.PoseLandmark.NOSE.value]
    left_elbow_landmark = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value]
    right_elbow_landmark = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value]
    left_wrist_landmark = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]
    right_wrist_landmark = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]

    left_nose_distance = int(hypot(left_elbow_landmark[0] - nose_landmark[0], left_elbow_landmark[1] - nose_landmark[1]))
    right_nose_distance = int(hypot(right_elbow_landmark[0] - nose_landmark[0], right_elbow_landmark[1] - nose_landmark[1]))
    wrist_distance_nose = int(hypot(right_wrist_landmark[0] - nose_landmark[0], right_wrist_landmark[1] - nose_landmark[1]))
    wrist_distance_y = int(abs(left_wrist_landmark[1] - right_wrist_landmark[1]))

    #the hands together pose
    #requires both hand landmarks to be close to each other
    hands_distance = int(hypot(left_wrist_landmark[0] - right_wrist_landmark[0], left_wrist_landmark[1] - right_wrist_landmark[1]))

    #calculate required angle measurements
    left_shoulder_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                         landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                         landmarks[mp_pose.PoseLandmark.LEFT_HIP.value])
    right_shoulder_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                          landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                          landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value])

    #here we will check for what pose it could be
    #current hierarchy of poses
    #left dab -> right dab -> psy -> hands_together -> t-pose

    if wrist_distance_y > 50:
        if right_nose_distance < 150:
            label = 'left dab'
            color = (0,255,0)
        elif left_nose_distance < 150:
            label = 'right dab'
            color = (0,255,0)
    elif (left_elbow_angle < 115 and left_elbow_angle > 65) and (right_elbow_angle < 295 and right_elbow_angle > 245) and wrist_distance_nose > 230:
        label = 'muscle man'
        color = (0,255,0)
    elif hands_distance < 200 and wrist_distance_nose < 110:
        label = 'relaxing'
        color = (0,255,0)
    elif left_elbow_angle > 165 and left_elbow_angle < 195 and right_elbow_angle < 195 and right_elbow_angle > 165 and left_shoulder_angle > 80 and left_shoulder_angle < 110 and right_shoulder_angle > 80 and right_shoulder_angle < 110:
        label = 'arms straight'
        color = (0,255,0)
    elif hands_distance < 80:
        label = 'hands together'
        color = (0,255,0)
            
        #print(left_knee_angle)
        #print(right_knee_angle)

    #here we will check if the pose was identified or not, and output the image
    cv2.putText(output_image, label, (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)

    #check if the resultant image is specified to be displayed
    if display:
    
        # Display the resultant image.
        plt.figure(figsize=[10,10])
        plt.imshow(output_image[:,:,::-1]);plt.title("Output Image");plt.axis('off');
        
    else:
        
        # Return the output image and the classified label.
        return output_image, label

# # Initialize the VideoCapture object to read from the webcam.
# camera_video = cv2.VideoCapture(0)

# # Initialize a resizable window.
# cv2.namedWindow('All Together Pose', cv2.WINDOW_NORMAL)
 
# # Iterate until the webcam is accessed successfully.
# while camera_video.isOpened():
    
#     # Read a frame.
#     ok, frame = camera_video.read()
    
#     # Check if frame is not read properly.
#     if not ok:
        
#         # Continue to the next iteration to read the next frame and ignore the empty camera frame.
#         continue
    
#     # Flip the frame horizontally for natural (selfie-view) visualization.
#     frame = cv2.flip(frame, 1)
    
#     # Get the width and height of the frame
#     frame_height, frame_width, _ =  frame.shape
    
#     # Resize the frame while keeping the aspect ratio.
#     frame = cv2.resize(frame, (int(frame_width * (640 / frame_height)), 640))
    
    
#     # Perform Pose landmark detection.
#     frame, landmarks = detectPose(frame, pose_video, draw=True, display=False)
    
    
#     # Check if the landmarks are detected.
#     if landmarks:
        
#         # Perform the Pose Classification.
#         frame, curr_pose = checkpose(landmarks, frame, display=False)
    
#     if curr_pose != 'Unknown Pose':
#         conn.send_command("volumeUp")
    
#     # Display the frame.
#     cv2.imshow('Pose Classification', frame)
    
#     # Wait until a key is pressed.
#     # Retreive the ASCII code of the key pressed
#     k = cv2.waitKey(1) & 0xFF
    
#     # Check if 'ESC' is pressed.
#     if(k == 27):
        
#         # Break the loop.
#         break
 
# # Release the VideoCapture object and close the windows.
# camera_video.release()