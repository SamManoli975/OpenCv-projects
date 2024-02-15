import cv2 as cv
import numpy as np

img = cv.imread('img2.jpg')
# Uncomment the line below if you want to resize the image
# img = cv.resize(img, (500, 500))
cv.imshow('image', img)

cv.waitKey(0)
cv.destroyAllWindows()
