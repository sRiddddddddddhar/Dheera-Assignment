import cv2
import time
import atexit
from fastapi import FastAPI
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .detector import HandDetector
from .tracker import HandTracker
from .gesture import GestureRecognizer
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
detector = HandDetector()
tracker = HandTracker()
gesture_detector = GestureRecognizer()
camera = cv2.VideoCapture(0)
prev_time = 0
mode_state = "both"
show_gesture_state = True
# Recording
recording = False
video_writer = None
output_file = "output.avi"
record_start_time = None
atexit.register(lambda: camera.release())
class Settings(BaseModel):
    mode: str
    show_gesture: bool
@app.post("/update_settings")
def update_settings(settings: Settings):
    global mode_state, show_gesture_state
    print("UPDATED:", settings)  # DEBUG
    mode_state = settings.mode
    show_gesture_state = settings.show_gesture
    return {"status": "updated"}
def generate_frames():
    global prev_time, recording, video_writer, record_start_time
    while True:
        success, frame = camera.read()
        if not success:
            break
        frame, detections = detector.detect(frame)
        detections = tracker.update(detections)
        for det in detections:
            x1, y1, x2, y2 = det["bbox"]
            hand_id = det["id"]
            gesture = ""
            if show_gesture_state:
                gesture = gesture_detector.detect(det["landmarks"])
            if mode_state == "box":
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            elif mode_state == "skeleton":
                detector.drawer.draw_landmarks(
                    frame,
                    det["landmarks"],
                    detector.mp_hands.HAND_CONNECTIONS
                )
            elif mode_state == "both":
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                detector.drawer.draw_landmarks(
                    frame,
                    det["landmarks"],
                    detector.mp_hands.HAND_CONNECTIONS
                )

            label = f"ID:{hand_id}"
            if show_gesture_state:
                label += f" {gesture}"
            cv2.putText(
                frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

        # FPS
        current_time = time.time()
        fps = 0 if prev_time == 0 else 1 / (current_time - prev_time)
        prev_time = current_time
        cv2.putText(frame, f"FPS: {int(fps)}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Timer
        if recording and record_start_time:
            elapsed = int(time.time() - record_start_time)
            cv2.putText(frame, f"REC {elapsed//60:02d}:{elapsed%60:02d}",
                        (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        # Recording
        if recording and video_writer is None:
            h, w, _ = frame.shape
            video_writer = cv2.VideoWriter(
                output_file,
                cv2.VideoWriter_fourcc(*'XVID'),
                20.0,
                (w, h)
            )
        if recording and video_writer:
            video_writer.write(frame)
        if not recording and video_writer:
            video_writer.release()
            video_writer = None
        _, buffer = cv2.imencode(".jpg", frame)
        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            buffer.tobytes() +
            b'\r\n'
        )

@app.get("/video")
def video_feed():
    return StreamingResponse(
        generate_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )

@app.get("/start_recording")
def start_recording():
    global recording, record_start_time
    recording = True
    record_start_time = time.time()
    return {"status": "recording started"}

@app.get("/stop_recording")
def stop_recording():
    global recording, record_start_time
    recording = False
    record_start_time = None
    return {"status": "recording stopped"}

@app.get("/download")
def download_video():
    return FileResponse(output_file, media_type='video/avi', filename="recorded.avi")