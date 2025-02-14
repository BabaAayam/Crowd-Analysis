import numpy as np
import cv2
from config import MIN_CONF

def detect_human(frame):
    # Initialize HOG descriptor with default people detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # Detect people in the image
    (boxes, weights) = hog.detectMultiScale(frame, winStride=(4, 4),
                                          padding=(8, 8), scale=1.05)
    
    # Filter detections by confidence
    filtered_boxes = []
    for i, (x, y, w, h) in enumerate(boxes):
        if weights[i] > MIN_CONF:
            filtered_boxes.append([x, y, w, h])
    
    return [filtered_boxes, []]
