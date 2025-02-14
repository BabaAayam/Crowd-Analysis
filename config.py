import datetime

# Video Path
VIDEO_CONFIG = {
    "VIDEO_CAP": 0,  # Webcam index
    "IS_CAM": True,  # Enable webcam mode
    "CAM_APPROX_FPS": 30,  # Target frame rate
    "HIGH_CAM": False,  # Not a high-mounted camera
    "START_TIME": datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
}

# YOLO Configuration
YOLO_CONFIG = {
    "MODEL_WEIGHTS": "YOLOv4/yolov4.weights",
    "MODEL_CONFIG": "YOLOv4/yolov4.cfg",

    "CONFIDENCE_THRESHOLD": 0.3,
    "NMS_THRESHOLD": 0.3
}

# Processing Configuration
SHOW_PROCESSING_OUTPUT = True
DATA_RECORD_RATE = 1  # Record data every frame
FRAME_SIZE = 1280  # Processing frame width
TRACK_MAX_AGE = 30  # Maximum frames to keep lost tracks

# Detection Configuration
MIN_CONF = 0.3  # Minimum confidence for detection
NMS_THRESH = 0.3  # Non-Maximum Suppression threshold
