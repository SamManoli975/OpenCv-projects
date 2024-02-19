import cv2 as cv
import os
from util import get_limits
from PIL import Image
# import numpy as np

yellow = [0, 255, 0] #RGB green
#create the window
cap = cv.VideoCapture(1)
cv.namedWindow('ColorDetection/frame', cv.WINDOW_NORMAL)


while True:
    ret, frame = cap.read()

    hsvImage = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    #get the limits from the function
    lower, upper = get_limits(color = yellow)

    #create the mask
    mask = cv.inRange(hsvImage, lower,upper)

    mask_ = Image.fromarray(mask)
    #create the bounding box based on the mask
    bounding_box = mask_.getbbox()
    #while the bounding box gives a value
    if bounding_box is not None:
        x, y, w, h = bounding_box#create the coordinates for the box
        frame = cv.rectangle(frame, (x, y), (w, h), (0, 255, 0), 5) #draw the box

    # print(bounding_box)
    cv.imshow('ColorDetection/frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):#if q is pressed exit
        break
    
#destroy window
cap.release()
cv.destroyAllWindows()
