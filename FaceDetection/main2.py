import cv2 as cv
import face_recognition
import numpy as np
import os

# Load known face encodings and names
known_faces_encodings = []
known_faces_names = []
known_faces_folder = "known_faces"  # Folder containing known face images

for filename in os.listdir(known_faces_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image = face_recognition.load_image_file(os.path.join(known_faces_folder, filename))
        encodings = face_recognition.face_encodings(image)

        if encodings:  # If the list is not empty
            encoding = encodings[0]
            known_faces_encodings.append(encoding)
            # Use the filename (without extension) as the name
            known_faces_names.append(os.path.splitext(filename)[0])  # Filename as name
        else:
            print(f"No faces found in image: {filename}")

# Function for detecting and recognizing faces
def detect_and_recognize(gray, frame):
    # Convert to RGB since face_recognition expects RGB images
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # Detect faces in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the detected face matches known faces
        matches = face_recognition.compare_faces(known_faces_encodings, face_encoding)
        name = "Unknown"  # Default name

        # If a match is found, get the name of the first matched face
        if True in matches:
            first_match_index = matches.index(True)
            name = known_faces_names[first_match_index]

        # Draw a rectangle around the face and display the name
        cv.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv.putText(frame, name, (left, top - 10), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    return frame

# Open the webcam
cap = cv.VideoCapture(0)

# Set the desired frame width and height for better quality
cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)  # Width
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)  # Height

cv.namedWindow('Face Detection and Recognition', cv.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Convert to grayscale (if needed, for other processing)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Apply face detection and recognition
    canvas = detect_and_recognize(gray, frame)

    # Show the result
    cv.imshow('Face Detection and Recognition', canvas)

    # Press 'q' to exit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv.destroyAllWindows()
