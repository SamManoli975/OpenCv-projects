import cv2 as cv
import numpy as np

#function to get the limits of the color we have to detect
def get_limits(color):
    
    c = np.uint8([[color]])
    hsvC = cv.cvtColor(c, cv.COLOR_BGR2HSV)
    lower = hsvC[0][0][0] -20,100,100
    upper = hsvC[0][0][0] +20,255,255

    lower = np.array(lower,dtype=np.uint8)
    upper = np.array(upper,dtype=np.uint8)

    return lower,upper