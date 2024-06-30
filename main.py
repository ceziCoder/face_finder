# -*- coding: utf-8 -*-
import cv2
# Wczytaj wytrenowany model CascadeClassifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("cant open cam")
    exit()

while True:
    ret, frame = capture.read()
    
    if not ret:
        print("cant read frame")
        continue
    
    if frame is None or frame.shape[0] == 0 or frame.shape[1] == 0:
        print("frame is bad dimension")
        continue

    cv2.imshow("VideoFrame", frame)

    key = cv2.waitKey(50)
    if key == 27:
        break

capture.release()
cv2.destroyAllWindows()