# Hand Detection and Tracking System

## Overview

This project is a real-time Hand Detection and Tracking System built using Computer Vision techniques.  
It detects hands from a webcam feed, tracks them with unique IDs, recognizes gestures, and provides an interactive web interface for visualization and control.

The system also supports video recording, gesture toggling, and multiple visualization modes, making it a complete end-to-end application.

---

## What It Does

- Detects hands using webcam input  
- Tracks hands with unique IDs  
- Recognizes gestures  
- Streams video in real-time  
- Allows recording and downloading  

---

## Project Structure

    hand-detection-app/
    │
    ├── backend/
    │   ├── main.py           # FastAPI server
    │   ├── detector.py       # Hand detection logic
    │   ├── tracker.py        # Tracking logic (IDs)
    │   ├── gesture.py        # Gesture recognition
    │
    ├── frontend/
    │   └── index.html        # UI interface
    │
    ├── requirements.txt      # Dependencies
    └── README.md             # Project documentation

---

## Quick Start

##Step 1: Clone the Repository

git clone
cd hand-detection-app

##Step 2: Create Virtual Environment

python -m venv venv
venv\Scripts\activate

##Step 3: Install Dependencies

pip install -r requirements.txt

##Step 4: Run Backend Server

uvicorn backend.main --reload

##Step 5: Open Frontend

Open the file:
frontend/index.html

---

## Tech Stack

- Backend: Python, FastAPI  
- Computer Vision: OpenCV, MediaPipe  
- Frontend: HTML, CSS, JavaScript  

---

## AI Tools Used

- ChatGPT (for debugging, UI design, and development support)

---

## Challenges Faced

-Dependency conflicts
    Issues with TensorFlow and protobuf versions
    Resolved by managing compatible versions
-MediaPipe compatibility
    Some versions didn’t support Python 3.12 properly
    Required environment adjustments
-MJPEG stream issues
    Stream freezing and flickering when updating UI
    Fixed by implementing backend-controlled state instead of restarting stream
-Tracking consistency
    Hand IDs increasing incorrectly after re-entry
    Solved with proper tracking logic reset
-UI/UX problems
    Layout issues and poor visibility of controls
    Improved with structured and user-friendly design
---

## Conclusion

This project demonstrates a complete real-time computer vision pipeline with an interactive UI.
