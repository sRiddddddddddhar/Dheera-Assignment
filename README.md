# Hand Detection and Tracking System

## Overview

This project is a real-time Hand Detection and Tracking System built using Computer Vision techniques.  
It detects hands from a webcam feed, tracks them with unique IDs, recognizes gestures, and provides an interactive web interface for visualization and control.

The system also supports video recording, gesture toggling, and multiple visualization modes, making it a complete end-to-end application.

---

## 🎯 What It Does

- Detects hands using webcam input  
- Tracks hands with unique IDs  
- Recognizes gestures  
- Streams video in real time  
- Allows video recording and downloading  

---

## 📁 Project Structure

```bash
hand-detection-app/
│
├── backend/
│   ├── main.py           # FastAPI server
│   ├── detector.py       # Hand detection logic
│   ├── tracker.py        # Tracking logic
│   ├── gesture.py        # Gesture recognition
│
├── frontend/
│   └── index.html        # User interface
│
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## 🚀 Quick Start

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd hand-detection-app
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Backend Server

```bash
uvicorn backend.main:app --reload
```

### Step 5: Open the Frontend

Open:

```bash
frontend/index.html
```

---

## 🛠 Tech Stack

- **Backend:** Python, FastAPI  
- **Computer Vision:** OpenCV, MediaPipe  
- **Frontend:** HTML, CSS, JavaScript  

---

## 🤖 AI Tools Used

- ChatGPT — Debugging, UI design, and development support  

---

## ⚡ Challenges Faced

### Dependency Conflicts
Issues with TensorFlow and protobuf version compatibility.  
Resolved by installing compatible package versions.

### MediaPipe Compatibility
Some MediaPipe versions did not fully support Python 3.12.  
Resolved by adjusting the Python environment and package versions.

### MJPEG Stream Issues
Video stream occasionally froze or flickered during UI updates.  
Resolved by implementing backend-controlled state management.

### Tracking Consistency
Hand IDs increased incorrectly when hands re-entered the frame.  
Resolved by improving tracking reset logic.

### UI/UX Challenges
Initial layouts had control visibility and usability issues.  
Resolved by redesigning the interface for better usability.

---

## Conclusion

This project demonstrates a complete real-time computer vision pipeline with hand detection, tracking, gesture recognition, and an interactive user interface.
