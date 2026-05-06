import cv2
import mediapipe as mp


class HandDetector:

    def __init__(self):

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.drawer = mp.solutions.drawing_utils


    def detect(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb)

        detections = []

        if results.multi_hand_landmarks:

            h, w, _ = frame.shape

            for hand_landmarks in results.multi_hand_landmarks:

                x_list = []
                y_list = []

                for lm in hand_landmarks.landmark:

                    x = int(lm.x * w)
                    y = int(lm.y * h)

                    x_list.append(x)
                    y_list.append(y)

                x1 = min(x_list)
                y1 = min(y_list)

                x2 = max(x_list)
                y2 = max(y_list)

                detections.append({
                    "bbox": (x1, y1, x2, y2),
                    "landmarks": hand_landmarks
                })

        return frame, detections