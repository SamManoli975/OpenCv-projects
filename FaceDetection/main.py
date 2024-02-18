import cv2 as cv#import
#reference the classifier i will use, it is a pre trained face detector
#the classifier is trained on a lot of images, so it can detect a lot of features
face_cascade = cv.CascadeClassifier('FaceDetection/haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(0)
cv.namedWindow('ColorDetection/frame', cv.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    #set the frame to greyscale
    grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #detect the faces in the frame
    faces = face_cascade.detectMultiScale(grey, 1.3, 5)

    #draw the rectangle around the face
    for (x, y, w, h) in faces:
        frame = cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)

    #show the frame
    cv.imshow('ColorDetection/frame', frame)

    #if q is pressed exit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

#destroy the window
cap.release()