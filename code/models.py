import cv2

class Camera(object):
    def __init__(self, cam_num = 0):
        self.cam_num = cam_num
        self.cap = None

    def initialize(self):
        self.cap = cv2.VideoCapture(self.cam_num)

    def get_frame(self):
        ret, self.last_frame = self.cap.read()
        return self.last_frame

    def acquire_movie(self, num_frames):
        movie = []


    def set_brightness(self, value = 0.5):
        self.cap.set(cv2.CAP_PROP_BRIGHTNESS, value)

    def get_brightness(self):
        return self.cap.get(cv2.CAP_PROP_BRIGHTNESS)

    def close_camera(self):
        self.cap.release()

    def __str__(self):
        return 'OpenCV Camera {}'.format(self.cam_num)



if __name__ == '__main__':
    cam = Camera()
    cam.initialize()

    # print(cam.get_frame().shape)
    cam.set_brightness(0.3)
    print(cam.get_brightness())

    cam.set_brightness(0.5)
    print(cam.get_brightness())


    cam.close_camera()