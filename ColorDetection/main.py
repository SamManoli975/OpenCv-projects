import cv2 as cv
import os
# import numpy as np

img = cv.imread('ColorDetection/images/venicecolor.jpg')
# img2 =cv.imread('./images/venicecolor.jpg')
# Uncomment the line below if you want to resize the image

# img = cv.resize(img2, (200, 200))
# cv.imshow('image', img2)
new_size = (450, 340)
img = cv.resize(img, new_size)

cv.imshow('image', img)

# def rescaleFrame(frame, scale=0.5):
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)
#     dimensions = (width, height)
# resize_img = cv.resize(img,(0, 0),fx=0.5, fy=0.7, interpolation = cv.INTER_AREA)

cv.waitKey(0)
cv.destroyAllWindows()
