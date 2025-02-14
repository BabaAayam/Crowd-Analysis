import time
import datetime
import numpy as np
import imutils
import cv2
from math import ceil
from scipy.spatial.distance import euclidean
from tracking import detect_human
from util import rect_distance
from config import FRAME_SIZE, SHOW_PROCESSING_OUTPUT



def process_video(frame):
    """
    Process a single frame from the webcam feed
    """
    try:


        
        # Resize frame to processing size
        print(f"Original frame size: {frame.shape}")
        frame = imutils.resize(frame, width=FRAME_SIZE)
        print(f"Resized frame to: {frame.shape}")

        
        # Detect humans in the frame
        print("Detecting humans...")
        human_boxes, expired = detect_human(frame)
        print(f"Detection complete. Found {len(human_boxes)} humans")



        # Process detected humans
        print(f"Detected {len(human_boxes)} humans")  # Debug print
        if len(human_boxes) > 0:
            # Perform crowd analysis
            process_crowd(frame, human_boxes)
            
            # Perform movement analysis
            process_movement(frame, human_boxes)
            
            # Display crowd count on frame
            count = len(human_boxes)
            cv2.putText(frame, f"People Count: {count}", (10, 50),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "People Count: 0", (10, 50),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
        return frame
        
    except Exception as e:
        print(f"Error processing frame: {str(e)}")
        return frame

def process_crowd(frame, human_boxes):
    """
    Analyze crowd density and behavior
    """
    # Calculate crowd density
    density = len(human_boxes)
    print(f"Crowd density: {density}")  # Debug print
    
    # Detect abnormal crowd behavior
    if density > 10:  # Example threshold
        cv2.putText(frame, "Warning: High Crowd Density!", (10, 100),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        print("Warning: High crowd density detected!")
    
    # Additional crowd analysis logic here

def process_movement(frame, human_boxes):
    """
    Analyze movement patterns
    """
    # Calculate movement vectors
    movement_vectors = []
    
    # Additional movement analysis logic here

def draw_analysis_results(frame, human_boxes):
    """
    Draw analysis results on the frame
    """
    # Draw bounding boxes
    for box in human_boxes:
        x, y, w, h = box
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Add other visualizations as needed
    
    return frame
