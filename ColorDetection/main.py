import cv2 as cv
import os
from util import get_limits
from PIL import Image
# import numpy as np

yellow = [0,255,255] 
cap = cv.VideoCapture(0)
cv.namedWindow('ColorDetection/frame', cv.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()

    hsvImage = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower, upper = get_limits(color = yellow)

    mask = cv.inRange(hsvImage, lower,upper)

    mask_ = Image.fromarray(mask)
    bounding_box = mask_.getbbox()
    if bounding_box is not None:
        x, y, w, h = bounding_box
        frame = cv.rectangle(frame, (x, y), (w, h), (0, 255, 0), 5)

    # print(bounding_box)
    cv.imshow('ColorDetection/frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
