boxes = pytesseract.image_to_boxes(img)

for box in boxes.splitlines():
    box = box.split()
    x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    
    # Draw the bounding box on the image
    cv.rectangle(img, (x, img.shape[0] - y), (w, img.shape[0] - h), (0, 255, 0), 2)

# Display the image with bounding boxes
cv.imshow('image_with_boxes', img)