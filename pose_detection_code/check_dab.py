#This is code that will test whether what im planning to do will work or not
#to get a dabbing pose, we need some things
#it only cares about the upper body
#for now, let one of the hands be higher than the other
#for now, choose right hand over left hand
#then the left elbow has to be close to the head

import cv2
from time import time
from math import hypot
import mediapipe as mp
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


def detectPose(image, pose, draw=False, display=False):
    '''
    This function performs the pose detection on the most prominent person in an image.
    Args:
        image:   The input image with a prominent person whose pose landmarks needs to be detected.
        pose:    The pose function required to perform the pose detection.
        draw:    A boolean value that is if set to true the function draw pose landmarks on the output image. 
        display: A boolean value that is if set to true the function displays the original input image, and the 
                 resultant image and returns nothing.
    Returns:
        output_image: The input image with the detected pose landmarks drawn if it was specified.
        results:      The output of the pose landmarks detection on the input image.
    '''
    
    # Create a copy of the input image.
    output_image = image.copy()
    
    # Convert the image from BGR into RGB format.
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Perform the Pose Detection.
    results = pose.process(imageRGB)
    
    # Check if any landmarks are detected and are specified to be drawn.
    if results.pose_landmarks and draw:
    
        # Draw Pose Landmarks on the output image.
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
        
    # Otherwise
    else:

        # Return the output image and the results of pose landmarks detection.
        return output_image, results

def checkDab(image, results, draw=False, display=False):
    '''
    This functions finds the postions of the hands, elbows, and nose, and 
    checks if the person is in a dab position or now
    Args:
        image: the input image with a prominent person whose dab pose needs to be found
        results: the output of the pose landmakrs detection on the input image
        draw: a boolean value that is if set to true the function writes the horizontal position on the output image
        display: a boolean value that is if set to true the function displays the resultant image and returns nothing
    Returns:
        output_image:       the same input image but with a boolean value of the dab in; 
        posture:        the posture(Dab or No Dab) of the person in an image
    '''

    #declare a variable to store if there is a dab or no dab
    person_dab = None

    #Get the height and width of the image.
    height, width, _ = image.shape

    #Create a copy of the input image to write the posture label on
    output_image = image.copy()

    #retrieve the y-coordinate of the left elbow
    left_elbow_landmark = (results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x * width,
                        results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y * height)

    #retrieve the y-coordinate of the right elbow
    right_elbow_landmark = (results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x * width,
                        results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y * height)

    #retrieve the y-coordinate of the left wrist
    left_y_wrist = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y * height)

    #retrieve the y-coordinate of the right wrist
    right_y_wrist = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y * height)

    #retrieve the x and y-coordinate of the nose
    nose_landmark = (results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * width,
                    results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * height)

    #calculate the euclidean distance between the left elbow and nose
    euclidean_distance_left = int(hypot(left_elbow_landmark[0] - nose_landmark[0],
                                left_elbow_landmark[1] - nose_landmark[1]))

    #calculate the euclidean distance between the right elbow and nose
    euclidean_distance_right = int(hypot(right_elbow_landmark[0] - nose_landmark[0],
                                right_elbow_landmark[1] - nose_landmark[1]))

    #calculate the distance between wrists
    wrist_distance = int(abs(left_y_wrist - right_y_wrist))

    #To get a dabbing pose, we need one of the wrists to be a greater height than the other
    #and the nose to be close to an elbow
    if wrist_distance > 50 and (euclidean_distance_left < 200 or euclidean_distance_right < 200):

        #set the dab value to true
        person_dab = 'DABBING'

        #set the color value to green
        color = (0,255,0)

    #otherwise
    else:

        #set the dab value to false
        person_dab = 'NO DAB'

        #set the color value to red
        color = (0,0,255)

    # Check if the Hands Joined status and hands distance are specified to be written on the output image.
    if draw:
 
        # Write the classified hands status on the image. 
        cv2.putText(output_image, person_dab, (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, color, 3)

    #Check if the output image is specified to be displayed
    if display:
 
        # Display the output image.
        plt.figure(figsize=[10,10])
        plt.imshow(output_image[:,:,::-1]);plt.title("Output Image");plt.axis('off');

    # Otherwise
    else:
    
        # Return the output image and the classified hands status indicating whether the hands are joined or not.
        return output_image, person_dab

# Initialize the VideoCapture object to read from the webcam.
camera_video = cv2.VideoCapture(0)
camera_video.set(3,1280)
camera_video.set(4,960)

# Create named window for resizing purposes.
cv2.namedWindow('Dab Detection', cv2.WINDOW_NORMAL)

#iterate until the webcam is accessed successfully
while camera_video.isOpened():

    # Read a frame.
    ok, frame = camera_video.read()
    
    # Check if frame is not read properly then continue to the next iteration to read the next frame.
    if not ok:
        continue

    # Flip the frame horizontally for natural (selfie-view) visualization.
    frame = cv2.flip(frame, 1)

    # Get the height and width of the frame of the webcam video.
    frame_height, frame_width, _ = frame.shape
    
    # Perform the pose detection on the frame.
    frame, results = detectPose(frame, pose_video, draw=True)
    
    # Check if the pose landmarks in the frame are detected.
    if results.pose_landmarks:

        # Check if the left and right hands are joined.
        frame, _ = checkDab(frame, results, draw=True)

    # Display the frame.
    cv2.imshow('Dabbing?', frame)
    
    # Wait for 1ms. If a key is pressed, retreive the ASCII code of the key.
    k = cv2.waitKey(1) & 0xFF
    
    # Check if 'ESC' is pressed and break the loop.
    if(k == 27):
        break

#release the videocapture object and close the window
camera_video.release()
cv2.destroyAllWindows()
