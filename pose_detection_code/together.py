#test how the pose_detection can work with multiple poses
#determine what our order of priority of poses is like
#the poses we'll use is dab and hands together

from time import time
from math import hypot

import cv2
import math
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt


# Initialize mediapipe pose class.
mp_pose = mp.solutions.pose
 
# Setup the Pose function for images.
pose_image = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5, model_complexity=1)
 
# Setup the Pose function for videos.
pose_video = mp_pose.Pose(static_image_mode=False, model_complexity=1, min_detection_confidence=0.7,
                          min_tracking_confidence=0.7)

# Initialize mediapipe drawing class.
mp_drawing = mp.solutions.drawing_utils 


#this basically combines the detectpose function from angle_detection and distance_detection
def detectPose(image, pose, draw=False, display=False):
    '''
    This function performs landmark detection on an image
    Args:
        image: the input image with a prominent person whose pose needs to be detected
        pose: the pose setup function required to perform the pose detection
        draw: a boolean value that if set to true the function draw pose landmakrs on the output image
        display: a boolean value that if set to true the function displays the original input image, and 
                 the resultant image and returns nothing
    Returns:
        output_image: the input image with the detected pose landmarks
        results: the output of the pose landmakrs detected on the input image
        landmarks: a list of detected landmarks converted into their original scale
    '''
    
    #create a copy of the input image
    output_image = image.copy()

    #convert the image from BGR into RGB format
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    #perform the pose detection
    results = pose.process(imageRGB)

    #retrieve the height and width of the input image
    height, width, _ = image.shape

    #initialize a list to store the detected landmarks
    landmarks = []

    #check if any landmakrs are detected
    if results.pose_landmakrs:

        # Draw Pose Landmarks on the output image.
        mp_drawing.draw_landmarks(image=output_image, landmark_list=results.pose_landmarks,
                                  connections=mp_pose.POSE_CONNECTIONS,
                                  landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255,255,255),
                                                                               thickness=3, circle_radius=3),
                                  connection_drawing_spec=mp_drawing.DrawingSpec(color=(49,125,237),
                                                                               thickness=2, circle_radius=2))
        
        # Iterate over the detected landmarks.
        for landmark in results.pose_landmarks.landmark:
            
            # Append the landmark into the list.
            landmarks.append((int(landmark.x * width), int(landmark.y * height),
                                  (landmark.z * width)))

    # Check if the original input image and the resultant image are specified to be displayed.
    if display:
    
        # Display the original input image and the resultant image.
        plt.figure(figsize=[22,22])
        plt.subplot(121);plt.imshow(image[:,:,::-1]);plt.title("Original Image");plt.axis('off');
        plt.subplot(122);plt.imshow(output_image[:,:,::-1]);plt.title("Output Image");plt.axis('off');
        
    # Otherwise
    else:
        
        # Return the output image and the found landmarks.
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
    x1, y1, _ = landmark1
    x2, y2, _ = landmark2
    x3, y3, _ = landmark3
 
    # Calculate the angle between the three points
    angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
    
    # Check if the angle is less than zero.
    if angle < 0:
 
        # Add 360 to the found angle.
        angle += 360
    
    # Return the calculated angle.
    return angle

def classifypose(landmarks, image, results, draw=False, display=False):
    '''
    This function determines what pose the person is in by checking the 
    positions and angle measurements of their landmarks
    Args:
        image: the input image with a prominent person whose pose needs to be detected
        results: the output of the pose landmakrs detection on the input image (distance measurement)
        landmarks: a list of detected landmakrs of the person (angle measurement)
    Output:
        output_image: the image with the detected pose landmark drawn and pose label written
        label: the classified pose label of the person in the output_image
    '''
    
    #declare a variable to store if there is a pose or no pose
    curr_pose = None

    #get the height and width of the image
    height, width, = image.shape

    #crate a copy of the input image to write the posture label
    output_image = image.copy()

    #get the xy coordinates of the ebows, wrists, and nose







# Initialize the VideoCapture object to read from the webcam.
camera_video = cv2.VideoCapture(0)