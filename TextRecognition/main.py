#import
import cv2 as cv
from pytesseract import pytesseract
pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

img = cv.imread('TextRecognition/media/roadsign1.jpg')
img = cv.resize(img, (640, 480))
# cv.imshow('image',img)


# reader = easyocr.Reader(['en'], gpu = False)
# text= reader.readtext(img)
# print(text)
text = pytesseract.image_to_string(img)
print(text)
cv.waitKey(0)

