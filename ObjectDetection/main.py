from ultralytics import YOLO
import cv2
from yolov5 import detect
import torch
model = YOLO("yolov5xu.pt")
img = cv2.imread("ObjectDetection/market.jpg")
img = cv2.resize(img, (640, 480))


results = model.predict(source="0", show=True)

print(results)

cv2.waitKey(0)