from config import YOLO_CONFIG, VIDEO_CONFIG, SHOW_PROCESSING_OUTPUT, DATA_RECORD_RATE, FRAME_SIZE, TRACK_MAX_AGE
from video_process import process_video
import cv2
import time

if FRAME_SIZE > 1920:
    print("Frame size is too large!")
    quit()
elif FRAME_SIZE < 640:
    print("Frame size is too small!")
    quit()

# Initialize webcam
cap = cv2.VideoCapture(VIDEO_CONFIG["VIDEO_CAP"])
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

# Set webcam properties
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_SIZE)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_SIZE * 9 // 16)

print("Starting live crowd analysis...")
try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from webcam")
            break
        
        # Process the frame
        process_video(frame)
        
        # Display the processed frame
        if SHOW_PROCESSING_OUTPUT:
            cv2.imshow('Crowd Analysis', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # Maintain frame rate
        time.sleep(1 / VIDEO_CONFIG["CAM_APPROX_FPS"])

except KeyboardInterrupt:
    print("Stopping live analysis...")
finally:
    cap.release()
    cv2.destroyAllWindows()
