#import
import cv2 as cv
from pytesseract import pytesseract
pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

img = cv.imread('TextRecognition/media/roadsign1.jpg')
img = cv.resize(img, (640, 480))
# cv.imshow('image',img)

# text = pytesseract.image_to_string(img)
# print(text)
detections = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

# Iterate over the detected words and draw bounding boxes
for i in range(len(detections['text'])):
    x, y, w, h = detections['left'][i], detections['top'][i], detections['width'][i], detections['height'][i]
    conf = int(detections['conf'][i])
    
    # Only draw bounding box if the confidence is high enough (adjust threshold as needed)
    if conf > 60:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        text = detections['text'][i]
        cv.putText(img, text, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv.LINE_AA)

# Display the image with bounding boxes around words
cv.imshow('image_with_boxes', img)

cv.waitKey(0)

