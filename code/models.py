import cv2

class Camera(object):
    def __init__(self, cam_num = 0):
        self.cam_num = cam_num
        self.cap = None
        self.is_initialzed = False
        self.last_frame = None

    def initialize(self):
        self.cap = cv2.VideoCapture(self.cam_num)
        if not self.cap.isOpened():
            raise Exception("Could not open video device")
        self.is_initialzed = True

    def isInitialized(self):
        return self.is_initialzed

    def get_frame(self):
        _, self.last_frame = self.cap.read()
        return self.last_frame

    def set_brightness(self, value = 0.5):
        self.cap.set(cv2.CAP_PROP_BRIGHTNESS, value)

    def get_brightness(self):
        return self.cap.get(cv2.CAP_PROP_BRIGHTNESS)

    def close_camera(self):
        self.set_brightness(0.5)    # Back to 'default' brightness
        self.cap.release()

    def __str__(self):
        return 'OpenCV Camera {}'.format(self.cam_num)



if __name__ == '__main__':
    cam = Camera()
    cam.initialize()

    cam.set_brightness(0.5)
    print(cam.get_brightness())

    import numpy as np
    frame = cam.get_frame()
    print("Max pixel value: {}, Min pixel value: {}".format(np.max(frame), np.min(frame)))

    cam.close_camera()