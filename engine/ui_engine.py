import cv2
import numpy as np
import time


class UIEngine:

    def __init__(self):

        self.dashboard_width = 360
        self.status_height = 70
        self.start_time = time.time()

    def draw_progress_bar(self, canvas, x, y, width, height, value):

        value = max(0, min(100, value))

        cv2.rectangle(
            canvas,
            (x, y),
            (x + width, y + height),
            (90, 90, 90),
            2
        )

        fill = int(width * value / 100)

        if value < 30:
            color = (0, 255, 0)
        elif value < 60:
            color = (0, 255, 255)
        else:
            color = (0, 0, 255)

        cv2.rectangle(
            canvas,
            (x, y),
            (x + fill, y + height),
            color,
            -1
        )

    def render(self, frame, data, fps):

        h, w = frame.shape[:2]

        canvas = np.zeros(
            (
                h + self.status_height,
                w + self.dashboard_width,
                3
            ),
            dtype=np.uint8
        )

        canvas[:] = (25, 25, 25)

        # ===============================
        # CAMERA
        # ===============================

        canvas[:h, :w] = frame

        # ===============================
        # DASHBOARD
        # ===============================

        cv2.rectangle(
            canvas,
            (w, 0),
            (w + self.dashboard_width, h),
            (40, 40, 40),
            -1
        )

        cv2.line(
            canvas,
            (w, 0),
            (w, h),
            (0, 255, 255),
            2
        )

        cv2.putText(
            canvas,
            "SafeDrive AI",
            (w + 25, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 255),
            2
        )

        # ===============================
        # ATTENTION SCORE
        # ===============================

        attention = max(
            0,
            100 - data["risk_score"]
        )

        # ===============================
        # SESSION TIME
        # ===============================

        elapsed = int(time.time() - self.start_time)

        mins = elapsed // 60

        secs = elapsed % 60

        # ===============================
        # INFO
        # ===============================

        info = [

            ("FPS", fps),

            ("Attention", f"{attention}%"),

            ("EAR", f"{data['ear']:.2f}"),

            ("MAR", f"{data['mar']:.2f}"),

            ("Eyes", data["eye_status"]),

            ("Yawning",
             "YES" if data["is_yawning"] else "NO"),

            ("Head",
             data["head_pose"]),

            ("Phone",
             "YES" if data["phone_detected"] else "NO"),

            ("Confidence",
             f"{data['phone_confidence']:.1f}%"),

            ("Blink Count",
             data["blink_count"]),

            ("Yawn Count",
             data["yawn_count"]),

            ("Session",
             f"{mins:02}:{secs:02}")

        ]

        y = 80

        for title, value in info:

            cv2.putText(
                canvas,
                title,
                (w + 20, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.58,
                (180, 180, 180),
                2
            )

            cv2.putText(
                canvas,
                str(value),
                (w + 190, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.58,
                (255, 255, 255),
                2
            )

            y += 34

        # ===============================
        # RISK BAR
        # ===============================

        cv2.putText(
            canvas,
            "Risk Level",
            (w + 20, y + 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255, 255, 255),
            2
        )

        self.draw_progress_bar(
            canvas,
            w + 20,
            y + 35,
            280,
            20,
            data["risk_score"]
        )

        cv2.putText(
            canvas,
            f"{data['risk_score']}%",
            (w + 310, y + 52),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (255, 255, 255),
            2
        )

        # ===============================
        # STATUS BAR
        # ===============================

        if data["driver_status"] == "SAFE":
            color = (0, 255, 0)

        elif data["driver_status"] == "WARNING":
            color = (0, 255, 255)

        else:
            color = (0, 0, 255)

        cv2.rectangle(
            canvas,
            (0, h),
            (w + self.dashboard_width, h + self.status_height),
            (18, 18, 18),
            -1
        )

        cv2.putText(
            canvas,
            f"Driver Status : {data['driver_status']}",
            (20, h + 45),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            color,
            2
        )

        # ===============================
        # PHONE INDICATOR
        # ===============================

        if data["phone_detected"]:

            cv2.putText(
                canvas,
                "PHONE DETECTED",
                (w + 20, h - 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2
            )

        return canvas
