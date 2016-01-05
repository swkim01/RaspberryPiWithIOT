import picamera, time
import cv2
import numpy as np
import sys, io

stream = io.BytesIO()

with picamera.PiCamera() as camera:
  camera.resolution = (640, 480)
  camera.framerate = 30
  while True:
    # Capture image from camera
    camera.capture(stream, format='jpeg', use_video_port=True)

    # Convert image from camera to a numpy array
    data = np.fromstring(stream.getvalue(), dtype=np.uint8)

    # Decode the numpy array image
    image = cv2.imdecode(data, cv2.CV_LOAD_IMAGE_COLOR)

    # Empty and return the in-memory stream to beginning
    stream.seek(0)
    stream.truncate(0)

    # Display the image
    cv2.imshow('image', image)

    # Wait for ESC to end program
    key = cv2.waitKey(10)
    if key == 27:
        break
