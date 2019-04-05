import numpy as np

from PyQt5.QtCore import Qt, QThread, QTimer
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QPushButton, QSlider
from pyqtgraph import ImageView



class StartWindow(QMainWindow):
    def __init__(self, camera, logger=None):
        super().__init__()

        self.camera = camera
        self.logger = logger
        if self.logger is not None:
            self.logger.info("Created Camera")

        self.central_widget = QWidget()

        # Widgets: Buttons, Sliders, ...
        self.button_start = QPushButton("Start", self.central_widget)
        self.button_stop = QPushButton("Stop", self.central_widget)
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 10)
        self.slider.setValue(self.camera.get_brightness())
        self.image_view = ImageView()

        # Signals
        self.button_start.clicked.connect(self.start)
        self.button_stop.clicked.connect(self.stop)
        self.slider.valueChanged.connect(self.update_brightness)

        # Timer for acquiring images at regular intervals
        self.acquisition_timer = QTimer()
        self.acquisition_timer.timeout.connect(self.update_image)

        # Widgets layout
        self.layout = QGridLayout(self.central_widget)
        self.layout.setColumnStretch(0, 9)
        self.layout.setColumnStretch(1, 1)
        self.layout.addWidget(self.button_start, 0, 1)
        self.layout.addWidget(self.button_stop, 1, 1)
        self.layout.addWidget(self.slider, 2, 1)
        self.layout.addWidget(self.image_view, 0, 0, 10, 1)

        self.setCentralWidget(self.central_widget)

    def start(self, update_interval=30):
        if not self.camera.isInitialized():
            self.camera.initialize()
        while self.camera.get_frame() is None:
            pass
        # self.movie_thread = MovieThread(self.camera)
        # self.movie_thread.start()
        self.acquisition_timer.start(update_interval)

    def stop(self):
        self.camera.close_camera()

    def update_image(self):
        frame = self.camera.get_frame()

        self.image_view.setImage(frame.T)
        if self.logger is not None:
            self.logger.info("Updated frame with Maximum in frame: {}, Minimum in frame: {}".format(np.max(frame), np.min(frame)))


    def update_brightness(self, value):
        value /= 10
        self.camera.set_brightness(value)
        if self.logger is not None:
            self.logger.info("Brightness set to: {}".format(value))


# class MovieThread(QThread):
#     def __init__(self, camera):
#         super().__init__()
#         self.camera = camera

#     def run(self):
#         self.camera.get_frame() #####################################
