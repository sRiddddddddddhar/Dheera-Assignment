import math
class HandTracker:
    def __init__(self):
        self.active_tracks = {}
        self.next_id = 0
    def update(self, detections):
        if len(detections) == 0:
            self.active_tracks = {}
            self.next_id = 0
            return detections
        new_tracks = {}
        for det in detections:
            x1, y1, x2, y2 = det["bbox"]
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2
            matched_id = None
            for hand_id, center in self.active_tracks.items():
                px, py = center
                distance = math.hypot(
                    cx - px,
                    cy - py
                )
                if distance < 80:
                    matched_id = hand_id
                    break
            if matched_id is None:
                matched_id = self.next_id
                self.next_id += 1
            det["id"] = matched_id
            new_tracks[matched_id] = (cx, cy)
        self.active_tracks = new_tracks
        return detections