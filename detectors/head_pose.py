import cv2
import numpy as np


class HeadPoseDetector:

    def __init__(self):

        pass

    def process(self, landmarks, frame):

        h, w, _ = frame.shape

        # MediaPipe landmark indices
        face_2d = []
        face_3d = []

        landmark_ids = [
            33,     # Left eye outer
            263,    # Right eye outer
            1,      # Nose tip
            61,     # Left mouth
            291,    # Right mouth
            199     # Chin
        ]

        for idx in landmark_ids:

            lm = landmarks.landmark[idx]

            x = int(lm.x * w)
            y = int(lm.y * h)

            face_2d.append([x, y])

            face_3d.append([x, y, lm.z * 3000])

        face_2d = np.array(face_2d, dtype=np.float64)
        face_3d = np.array(face_3d, dtype=np.float64)

        focal_length = w

        cam_matrix = np.array([
            [focal_length, 0, w / 2],
            [0, focal_length, h / 2],
            [0, 0, 1]
        ])

        dist_matrix = np.zeros((4, 1), dtype=np.float64)

        success, rotation_vec, translation_vec = cv2.solvePnP(
            face_3d,
            face_2d,
            cam_matrix,
            dist_matrix,
            flags=cv2.SOLVEPNP_ITERATIVE
        )

        if not success:

            return {
                "head_pose": "UNKNOWN",
                "pitch": 0,
                "yaw": 0,
                "roll": 0
            }

        rotation_matrix, _ = cv2.Rodrigues(rotation_vec)

        angles, _, _, _, _, _ = cv2.RQDecomp3x3(rotation_matrix)

        pitch = angles[0] * 360
        yaw = angles[1] * 360
        roll = angles[2] * 360

        # Determine direction
        direction = "FORWARD"

        if yaw < -15:
            direction = "LEFT"

        elif yaw > 15:
            direction = "RIGHT"

        elif pitch < -15:
            direction = "DOWN"

        elif pitch > 15:
            direction = "UP"

        return {

            "head_pose": direction,

            "pitch": round(pitch, 2),

            "yaw": round(yaw, 2),

            "roll": round(roll, 2)

        }
