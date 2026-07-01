import cv2
import mediapipe as mp

import config

from detectors.eye_detector import EyeDetector
from detectors.blink_detector import BlinkDetector
from detectors.yawn_detector import YawnDetector
from detectors.head_pose import HeadPoseDetector
from detectors.phone_detector import PhoneDetector

from engine.risk_engine import RiskEngine
from engine.alarm import Alarm
from engine.logger import EventLogger


class VisionEngine:

    def __init__(self):

        # -----------------------------
        # MediaPipe Face Mesh
        # -----------------------------
        self.mp_face_mesh = mp.solutions.face_mesh

        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=config.MAX_NUM_FACES,
            refine_landmarks=True,
            min_detection_confidence=config.MIN_DETECTION_CONFIDENCE,
            min_tracking_confidence=config.MIN_TRACKING_CONFIDENCE
        )

        self.drawer = mp.solutions.drawing_utils

        self.spec = self.drawer.DrawingSpec(
            color=(0, 255, 0),
            thickness=1,
            circle_radius=1
        )

        # -----------------------------
        # AI Modules
        # -----------------------------
        self.eye_detector = EyeDetector()
        self.blink_detector = BlinkDetector()
        self.yawn_detector = YawnDetector()
        self.head_detector = HeadPoseDetector()
        self.phone_detector = PhoneDetector()

        # -----------------------------
        # Engine Modules
        # -----------------------------
        self.risk_engine = RiskEngine()
        self.alarm = Alarm()
        self.logger = EventLogger()

    def process(self, frame):

        # -----------------------------
        # PHONE DETECTION (YOLO)
        # -----------------------------
        frame, phone_data = self.phone_detector.process(frame)

        # -----------------------------
        # FACE MESH
        # -----------------------------
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.face_mesh.process(rgb)

        data = {

            "ear": 0.0,
            "eye_status": "NO FACE",
            "blink_count": 0,
            "closed_frames": 0,

            "mar": 0.0,
            "is_yawning": False,
            "yawn_count": 0,

            "head_pose": "NO FACE",
            "pitch": 0.0,
            "yaw": 0.0,
            "roll": 0.0,

            "phone_detected": phone_data["phone_detected"],
            "phone_confidence": phone_data["phone_confidence"],
            "phone_bbox": phone_data["phone_bbox"],

            "risk_score": 0,
            "driver_status": "SAFE",

            "alarm": False,
            "alarm_reason": "",

            "risk_reasons": []

        }

        if results.multi_face_landmarks:

            landmarks = results.multi_face_landmarks[0]

            # ---------------------------------------
            # Draw Face Mesh
            # ---------------------------------------

            self.drawer.draw_landmarks(
                image=frame,
                landmark_list=landmarks,
                connections=self.mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=self.spec,
                connection_drawing_spec=self.spec
            )

            # ---------------------------------------
            # Draw Eye Landmarks
            # ---------------------------------------

            frame = self.eye_detector.draw_eyes(
                frame,
                landmarks
            )

            # ---------------------------------------
            # Blink Detection
            # ---------------------------------------

            blink_data = self.blink_detector.process(
                landmarks,
                frame
            )

            # ---------------------------------------
            # Yawn Detection
            # ---------------------------------------

            yawn_data = self.yawn_detector.process(
                landmarks,
                frame
            )

            # ---------------------------------------
            # Head Pose
            # ---------------------------------------

            head_data = self.head_detector.process(
                landmarks,
                frame
            )

            # ---------------------------------------
            # Risk Calculation
            # ---------------------------------------

            risk_data = self.risk_engine.calculate(
                blink_data,
                yawn_data,
                head_data,
                phone_data
            )

            # ---------------------------------------
            # Merge All Results
            # ---------------------------------------

            data.update(blink_data)
            data.update(yawn_data)
            data.update(head_data)
            data.update(phone_data)
            data.update(risk_data)

            # ---------------------------------------
            # Alarm
            # ---------------------------------------

            if data["alarm"]:

                self.alarm.trigger(
                    data["alarm_reason"]
                )

                self.logger.log(
                    data["alarm_reason"],
                    data["risk_score"],
                    data["driver_status"]
                )

        return frame, data
