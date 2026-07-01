import cv2
import config


class Camera:

    def __init__(self):

        self.cap = cv2.VideoCapture(config.CAMERA_INDEX)

        if not self.cap.isOpened():
            raise Exception("Unable to access camera.")

    def get_frame(self):

        success, frame = self.cap.read()

        if not success:
            return None

        return frame

    def release(self):

        self.cap.release()
