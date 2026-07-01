from scipy.spatial import distance


class YawnDetector:

    def __init__(self):

        self.yawn_count = 0

        self.yawning = False

        self.threshold = 0.60

    def process(self, landmarks, frame):

        h, w, _ = frame.shape

        top = landmarks.landmark[13]
        bottom = landmarks.landmark[14]

        left = landmarks.landmark[78]
        right = landmarks.landmark[308]

        top_pt = (int(top.x * w), int(top.y * h))
        bottom_pt = (int(bottom.x * w), int(bottom.y * h))

        left_pt = (int(left.x * w), int(left.y * h))
        right_pt = (int(right.x * w), int(right.y * h))

        vertical = distance.euclidean(top_pt, bottom_pt)
        horizontal = distance.euclidean(left_pt, right_pt)

        mar = vertical / horizontal

        if mar > self.threshold:

            if not self.yawning:

                self.yawn_count += 1

            self.yawning = True

        else:

            self.yawning = False

        return {

            "mar": mar,

            "is_yawning": self.yawning,

            "yawn_count": self.yawn_count

        }
