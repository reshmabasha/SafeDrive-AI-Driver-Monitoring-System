from scipy.spatial import distance
import config


class BlinkDetector:

    LEFT_EYE = [33, 160, 158, 133, 153, 144]
    RIGHT_EYE = [362, 385, 387, 263, 373, 380]

    def __init__(self):

        self.blink_count = 0

        self.closed_frames = 0

        self.eye_closed = False

    def eye_aspect_ratio(self, eye):

        A = distance.euclidean(eye[1], eye[5])

        B = distance.euclidean(eye[2], eye[4])

        C = distance.euclidean(eye[0], eye[3])

        return (A + B) / (2 * C)

    def process(self, landmarks, frame):

        h, w, _ = frame.shape

        left = []

        right = []

        for idx in self.LEFT_EYE:

            point = landmarks.landmark[idx]

            left.append(
                (
                    int(point.x * w),
                    int(point.y * h)
                )
            )

        for idx in self.RIGHT_EYE:

            point = landmarks.landmark[idx]

            right.append(
                (
                    int(point.x * w),
                    int(point.y * h)
                )
            )

        leftEAR = self.eye_aspect_ratio(left)

        rightEAR = self.eye_aspect_ratio(right)

        ear = (leftEAR + rightEAR) / 2

        if ear < config.EAR_THRESHOLD:

            self.closed_frames += 1

            self.eye_closed = True

        else:

            if self.eye_closed:

                self.blink_count += 1

            self.closed_frames = 0

            self.eye_closed = False

        return {

            "ear": ear,

            "eye_status": "CLOSED" if self.eye_closed else "OPEN",

            "blink_count": self.blink_count,

            "closed_frames": self.closed_frames,

            "is_drowsy": self.closed_frames > config.DROWSY_FRAMES

        }
