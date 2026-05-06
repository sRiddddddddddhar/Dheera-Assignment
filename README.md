# Hand Detection and Tracking System

## Overview

This project is a real-time Hand Detection and Tracking System built using Computer Vision techniques.  
It detects hands from a webcam feed, tracks them with unique IDs, recognizes gestures, and provides an interactive web interface for visualization and control.

The system also supports video recording, gesture toggling, and multiple visualization modes, making it a complete end-to-end application.

---

## What It Does

This system performs the following:

- Detects hands using webcam input  
- Tracks hands with unique IDs  
- Recognizes gestures  
- Streams video in real-time  
- Allows recording and downloading  

---

## Quick Start

### 1. Install Dependencies

pip install -r requirements.txt

### 2. Run Backend

uvicorn backend.main:app --reload

### 3. Open Frontend

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

- Dependency conflicts  
- MediaPipe compatibility issues  
- Streaming issues  
- Tracking logic fixes  

---

## Conclusion

This project demonstrates a complete real-time computer vision pipeline with an interactive UI.
