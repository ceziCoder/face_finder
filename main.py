# -*- coding: utf-8 -*-
import cv2

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Nie można otworzyć kamery")
    exit()

while True:
    ret, frame = capture.read()
    
    if not ret:
        print("Nie można odczytać klatki")
        continue
    
    if frame is None or frame.shape[0] == 0 or frame.shape[1] == 0:
        print("Klatka ma nieprawidłowe wymiary")
        continue

    cv2.imshow("VideoFrame", frame)

    key = cv2.waitKey(50)
    if key == 27:
        break

capture.release()
cv2.destroyAllWindows()