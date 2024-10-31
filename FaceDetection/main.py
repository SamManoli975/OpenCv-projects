import cv2 as cv

# Reference the classifier files
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv.CascadeClassifier('haarcascade_smile.xml')

# Ensure classifiers are loaded correctly
if face_cascade.empty() or smile_cascade.empty():
    print("Error loading cascade classifiers")
    exit()

# Function for detecting face and smile
def detect(gray, frame): 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
    for (x, y, w, h) in faces: 
        cv.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2) 
        roi_gray = gray[y:y + h, x:x + w] 
        roi_color = frame[y:y + h, x:x + w] 
        # Smile detection within the detected face region
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 15) 
        for (sx, sy, sw, sh) in smiles: 
            cv.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2) 
    return frame 

# Open the webcam
cap = cv.VideoCapture(0)
cv.namedWindow('ColorDetection/frame', cv.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    # Convert to grayscale
    grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Apply face and smile detection
    canvas = detect(grey, frame) 

    # Show the result
    cv.imshow('ColorDetection/frame', canvas)

    # Press 'q' to exit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv.destroyAllWindows()
