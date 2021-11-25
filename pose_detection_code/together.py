#test how the pose_detection can work with multiple poses
#determine what our order of priority of poses is like
#the poses we'll use is dab and hands together

import cv2
import pyautogui
from time import time
from math import hypot
import mediapipe as mp
import matplotlib.pyplot as plt

