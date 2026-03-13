import cv2
from ultralytics import YOLO
import pyttsx3
import threading
import time

# 1. Initialize offline TTS
engine = pyttsx3.init()
engine.setProperty('rate', 150) # Speed of speech

# Threading function so speaking doesn't freeze the camera
def speak_async(text):
    engine.say(text)
    engine.runAndWait()

# 2. Load the model
model = YOLO("yolov8n.pt") 
cap = cv2.VideoCapture(0)

# Optimization variables
frame_count = 0
skip_frames = 5  # Only process 1 out of every 5 frames
last_spoken = {} # Track what was said and when
cooldown_seconds = 3 # Wait 3 seconds before repeating the same object

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame_count += 1
    annotated_frame = frame # Default to raw frame if we skip detection

    # 3. Frame Skipping Logic
    if frame_count % skip_frames == 0:
        # 4. Reduce imgsz to 320 for much faster CPU inference
        results = model(frame, imgsz=320, verbose=False)[0] 
        annotated_frame = results.plot()

        for box in results.boxes:
            class_id = int(box.cls[0])
            label = model.names[class_id]
            
            # 5. Cooldown Logic: Don't spam the audio
            current_time = time.time()
            if label not in last_spoken or (current_time - last_spoken[label] > cooldown_seconds):
                print(f"Announcing: {label}")
                last_spoken[label] = current_time
                
                # Run audio in a separate background thread
                threading.Thread(target=speak_async, args=(f"{label} ahead",), daemon=True).start()

    # Display the feed
    cv2.imshow("Assistive Vision (Optimized)", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()