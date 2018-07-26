import cv2
import numpy as np
from multiprocessing import Process, Pipe


class Camera:
    def __init__(self, **kwargs):
        self.mirror = kwargs.get("mirror", False)
        self.cam = cv2.VideoCapture(kwargs.get("device", 0))
        self.output = None
        self.paused = False

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    @property
    def image(self):
        ret_val, img = self.cam.read()
        if self.mirror:
            img = cv2.flip(img, 1)
        self.output = img
        return img


if __name__ == "__main__":
    cam = Camera(mirror=True)
    while 1:
        cv2.imshow('my webcam', cam.image)
        if cv2.waitKey(1) == 27:
            break  # esc to quit