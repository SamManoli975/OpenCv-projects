import cv2 as cv#import
#reference the classifier i will use, it is a pre trained face detector
#the classifier is trained on a lot of images, so it can detect a lot of features
face_cascade = cv.CascadeClassifier('FaceDetection/haarcascade_frontalface_default.xml')
smile_cascade = cv.CascadeClassifier('FaceDetection/haarcascade_smile.xml')

#function for detecting face and smile
def detect(gray, frame): 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
    #one loop for faces
    for (x, y, w, h) in faces: 
        cv.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2) 
        roi_gray = gray[y:y + h, x:x + w] 
        roi_color = frame[y:y + h, x:x + w] 
        #adding scaleFactor and minNeighbours
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20) 
        #smile loop inside faces since one smile per face (hopefully)
        for (sx, sy, sw, sh) in smiles: 
            cv.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2) 
    return frame 

cap = cv.VideoCapture(1)
cv.namedWindow('ColorDetection/frame', cv.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    #set the frame to greyscale
    grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #detect the faces in the frame
    faces = face_cascade.detectMultiScale(grey, 1.3, 5)
    smile = smile_cascade.detectMultiScale(grey, 1.3, 5)

    canvas = detect(grey, frame) 
    #draw the rectangle around the face
    # for (x, y, w, h) in faces:
    #     frame = cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)
    # for (x, y, w, h) in smile:
    #     frame = cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)

    #show the frame
    cv.imshow('ColorDetection/frame', canvas)

    #if q is pressed exit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

#destroy the window
cap.release()