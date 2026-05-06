class GestureRecognizer:
    def detect(self, landmarks):
        tips = [4, 8, 12, 16, 20]
        fingers = []
        for tip in tips[1:]:
            if landmarks.landmark[tip].y < landmarks.landmark[tip-2].y:
                fingers.append(1)
            else:
                fingers.append(0)
        count = sum(fingers)
        if count == 4:
            return "Open Palm"
        elif count == 0:
            return "Fist"
        elif count == 2:
            return "Peace"
        else:
            return "Unknown"