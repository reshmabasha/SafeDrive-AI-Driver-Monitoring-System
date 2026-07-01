import cv2

# MediaPipe Face Mesh landmark indices
LEFT_EYE = [
    33, 133, 160, 159, 158, 157, 173,
    144, 145, 153, 154, 155
]

RIGHT_EYE = [
    362, 263, 387, 386, 385, 384, 398,
    373, 374, 380, 381, 382
]


class EyeDetector:

    def __init__(self):
        pass

    def draw_eyes(self, frame, face_landmarks):

        h, w, _ = frame.shape

        # Draw Left Eye
        for idx in LEFT_EYE:

            point = face_landmarks.landmark[idx]

            x = int(point.x * w)
            y = int(point.y * h)

            cv2.circle(frame, (x, y), 2, (0, 0, 255), -1)

        # Draw Right Eye
        for idx in RIGHT_EYE:

            point = face_landmarks.landmark[idx]

            x = int(point.x * w)
            y = int(point.y * h)

            cv2.circle(frame, (x, y), 2, (255, 0, 0), -1)

        return frame
