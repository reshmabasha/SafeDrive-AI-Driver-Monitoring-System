from ultralytics import YOLO
import cv2


class PhoneDetector:

    def __init__(self):

        # Better model
        self.model = YOLO("yolov8s.pt")

        self.confidence = 0.30

        self.frame_count = 0

        self.skip_frames = 3

        self.last_result = {
            "phone_detected": False,
            "phone_confidence": 0.0,
            "phone_bbox": None
        }

    def process(self, frame):

        self.frame_count += 1

        # Run YOLO every 3 frames
        if self.frame_count % self.skip_frames != 0:
            return frame, self.last_result

        results = self.model(
            frame,
            verbose=False,
            conf=self.confidence
        )

        detected = False

        confidence = 0.0

        bbox = None

        annotated = frame.copy()

        for result in results:

            if result.boxes is None:
                continue

            for box in result.boxes:

                cls = int(box.cls[0])

                name = self.model.names[cls]

                if name != "cell phone":
                    continue

                conf = float(box.conf[0])

                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0]
                )

                detected = True

                confidence = conf

                bbox = (x1, y1, x2, y2)

                cv2.rectangle(
                    annotated,
                    (x1, y1),
                    (x2, y2),
                    (0, 0, 255),
                    3
                )

                cv2.putText(
                    annotated,
                    f"PHONE {conf*100:.1f}%",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2
                )

        self.last_result = {

            "phone_detected": detected,

            "phone_confidence": round(confidence * 100, 2),

            "phone_bbox": bbox

        }

        return annotated, self.last_result
