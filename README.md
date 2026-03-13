# EchoSight: Low-Latency Assistive Vision System

A real-time, wearable object detection system engineered to assist individuals with visual impairments. This project leverages Computer Vision and Machine Learning to process video inputs and convert visual data into immediate, spatial audio feedback. 

The system is specifically optimized for low-latency performance on edge devices, prioritizing user safety and independence.

## 🚀 Key Features & Engineering Highlights

* **Real-Time Object Detection:** Utilizes Ultralytics YOLOv8 Nano (`yolov8n.pt`) for high-speed, accurate inference.
* **Asynchronous Audio Pipeline:** Implements Python `threading` alongside `pyttsx3` offline text-to-speech. This decouples the audio generation from the main vision loop, preventing camera freeze and ensuring a continuous, smooth video feed.
* **Edge-Optimized Processing:** * **Frame-Skipping:** Analyzes 1 out of every 5 frames to drastically reduce CPU workload while maintaining the illusion of instantaneous detection.
    * **Resolution Scaling:** Reduces YOLO inference resolution (`imgsz=320`) to accelerate processing times on CPU-constrained hardware.
* **Smart Audio Cooldown Logic:** Incorporates a time-based memory dictionary to track announced objects, preventing auditory spam and sensory overload when users are stationary.

## 🛠️ Tech Stack

* **Language:** Python
* **Computer Vision:** OpenCV (`cv2`)
* **Machine Learning:** Ultralytics YOLOv8
* **Audio/TTS:** `pyttsx3` (Offline for reliability in low-connectivity areas)

## ⚙️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Saksham52/Smart-Assistive-Armlet.git](https://github.com/Saksham52/Smart-Assistive-Armlet.git)
    cd Smart-Assistive-Armlet
    ```

2.  **Create a virtual environment (Recommended):**
    ```bash
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the system:**
    ```bash
    python app.py
    ```
    *Note: Press `q` in the video window to safely exit the application.*

## 🧠 Future Scope
* Integration with depth cameras for accurate distance calculation.
* Spatial audio routing (left/right ear audio based on bounding box coordinates).
* Deployment on NVIDIA Jetson / Raspberry Pi hardware using TensorRT optimization.

---
**Author:** Saksham Adhau  
**Role:** Project Lead  
**Links:** [LinkedIn](https://linkedin.com/in/saksham-adhau-44583220a) | [GitHub](https://github.com/Saksham52)
