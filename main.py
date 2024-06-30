# -*- coding: utf-8 -*-
import cv2

# write model CascadeClassifier
face_cascade = cv2.CascadeClassifier(
     "haarcascades/haarcascade_frontalface_default.xml"
)
if face_cascade.empty():
    print("Could not load cascade classifier")
    exit()
capture = cv2.VideoCapture(0)


if not capture.isOpened():
    print("cant open cam")
    exit()

while True:
    ret, frame = capture.read()

    if not ret:
        print("cant read frame")
        continue
    # detect face
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=5, maxSize=(50, 50)
    )

    # Print detected faces for debugging
    if len(faces) > 0:
        print(f"Detected faces: {faces}")
    else:
        print("No faces detected")

    # Draw a rectangle around each face
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 4)

    if frame is None or frame.shape[0] == 0 or frame.shape[1] == 0:
        print("frame is bad dimension")
        continue

    cv2.imshow("VideoFrame", frame)
    cv2.imshow("GrayFrame", gray)

    # Break the loop on ESC key press
    if cv2.waitKey(50) & 0xFF == 27:
        break

capture.release()
cv2.destroyAllWindows()
