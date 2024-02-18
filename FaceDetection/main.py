import cv2 as cv
face_cascade = cv.CascadeClassifier('FaceDetection/haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(0)
cv.namedWindow('ColorDetection/frame', cv.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grey, 1.3, 5)

    for (x, y, w, h) in faces:
        frame = cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)

    cv.imshow('ColorDetection/frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()