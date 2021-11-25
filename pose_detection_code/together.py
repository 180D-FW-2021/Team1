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
