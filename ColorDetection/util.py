import cv2 as cv
import numpy as np

def get_limits(color):
    
    c = np.uint8([[color]])
    hsvC = cv.cvtColor(c, cv.COLOR_BGR2HSV)
    lower = hsvC[0][0][0] -10,100,100
    upper = hsvC[0][0][0] +10,255,255

    lower = np.array(lower,dtype=np.uint8)
    upper = np.array(upper,dtype=np.uint8)

    return lower,upper