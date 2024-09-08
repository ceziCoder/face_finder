# Face Detection Script Using OpenCV

## Overview
This Python script detects faces in real-time using a webcam feed, leveraging OpenCV and the Haar Cascade classifier for frontal face detection. The script captures video from the default webcam, processes each frame to detect faces, and draws rectangles around the detected faces in the live video feed.

## Requirements

1. **Python 3.x**
2. **OpenCV**: Library for computer vision tasks.

You can install the required dependencies by running:
```bash
pip install opencv-python opencv-python-headless
```

## How It Works

1. **Initialize the Cascade Classifier**: 
   The Haar Cascade classifier `haarcascade_frontalface_default.xml` is used to detect faces in a frame.
   
2. **Capture Video from Webcam**: 
   The script opens the webcam (using `cv2.VideoCapture(0)`) and continuously captures frames.

3. **Face Detection**:
   Each captured frame is converted to grayscale to improve detection accuracy and performance. The classifier then searches for faces within a defined range of sizes (50x50 to 300x300 pixels).

4. **Display Detected Faces**:
   The script draws rectangles around the detected faces and displays the result in a window.

5. **Exit on ESC Key**: 
   The loop continues until the user presses the ESC key (`key code 27`).

## Script Breakdown

### 1. Importing Libraries
The script imports `cv2` for video capture, face detection, and image processing.
```python
import cv2
```

### 2. Loading the Haar Cascade Classifier
The Haar Cascade classifier file is loaded using OpenCV’s `CascadeClassifier`.
```python
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
if face_cascade.empty():
    print("Could not load cascade classifier")
    exit()
```

### 3. Capturing Video from Webcam
OpenCV captures video from the default webcam. The script checks if the webcam is properly opened.
```python
capture = cv2.VideoCapture(0)
if not capture.isOpened():
    print("cant open cam")
    exit()
```

### 4. Face Detection Logic
For each frame:
- The frame is converted to grayscale using `cv2.cvtColor`.
- The `detectMultiScale` method is used to detect faces in the grayscale image, with the following parameters:
  - `scaleFactor=1.1`: Specifies how much the image size is reduced at each image scale.
  - `minNeighbors=5`: Specifies how many neighbors each rectangle should have to retain it.
  - `minSize=(50, 50)`, `maxSize=(300, 300)`: The minimum and maximum size of the detected faces.
  
Detected faces are outlined with rectangles.
```python
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50), maxSize=(300, 300))

for x, y, w, h in faces:
    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 4)
```

### 5. Display the Frame
The processed frame with detected faces is displayed in a window named `"VideoFrame"`.
```python
cv2.imshow("VideoFrame", frame)
```

### 6. Exit on ESC Key Press
The script listens for the ESC key to exit the loop and release the webcam.
```python
if cv2.waitKey(50) & 0xFF == 27:
    break
```

### 7. Releasing Resources
After exiting, the script releases the webcam and closes all windows.
```python
capture.release()
cv2.destroyAllWindows()
```

## How to Run

1. Ensure that you have a webcam connected to your machine.
2. Install OpenCV if it's not installed:
   ```bash
   pip install opencv-python
   ```
3. Run the script:
   ```bash
   python3 face_detection.py
   ```
4. A window should appear displaying the webcam feed. If a face is detected, a rectangle will be drawn around it.
5. Press the ESC key to exit the program.

## Troubleshooting

- **No webcam detected**: Make sure the webcam is properly connected and accessible. If you have multiple webcams, you may need to change the `cv2.VideoCapture(0)` to a different index, such as `cv2.VideoCapture(1)` for a second webcam.
  
- **No faces detected**: Check if the `haarcascade_frontalface_default.xml` file is loaded correctly. The script currently limits face sizes between 50x50 and 300x300 pixels; adjust these sizes for your use case.

- **Performance issues**: Consider lowering the frame resolution or increasing the detection `scaleFactor` for faster performance.

## License

This project is released under the MIT License.
