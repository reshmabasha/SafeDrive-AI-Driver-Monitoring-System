import cv2
import time

import config

from core.camera import Camera
from core.vision_engine import VisionEngine
from engine.ui_engine import UIEngine


def main():

    print("=" * 70)
    print("      SafeDrive AI - Intelligent Driver Monitoring System")
    print("=" * 70)

    camera = Camera()
    vision = VisionEngine()
    ui = UIEngine()

    previous_time = time.time()

    while True:

        frame = camera.get_frame()

        if frame is None:
            print("[INFO] Camera disconnected.")
            break

        # -----------------------------
        # AI Processing
        # -----------------------------
        frame, data = vision.process(frame)

        # -----------------------------
        # FPS Calculation
        # -----------------------------
        current_time = time.time()

        fps = 1 / max(current_time - previous_time, 0.0001)

        previous_time = current_time

        # -----------------------------
        # Render Dashboard
        # -----------------------------
        dashboard = ui.render(
            frame,
            data,
            int(fps)
        )

        cv2.imshow(
            config.WINDOW_NAME,
            dashboard
        )

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
