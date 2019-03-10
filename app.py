from functools import partial

import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton


# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_BRIGHTNESS, 1.0)
# cap.set(cv2.CAP_PROP_GAIN, .01)
# cap.set(cv2.CAP_PROP_EXPOSURE, .01)


# while True:
#     ret, frame = cap.read()

#     # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     cv2.imshow('Frame', frame)

#     if cv2.waitKey(30) & 0xFF == ord('q'):
#         break


# cap.release()
# cv2.destroyAllWindows()


class ClickCount(object):
    def __init__(self, count = 0):
        self.count = count

    def get_count(self):
        return self.count

    def new_click(self):
        self.count += 1
        return self.count



app = QApplication([])
win = QMainWindow()

# count = ClickCount(0)

# button = QPushButton(str(count.get_count()))
# button.clicked.connect(lambda _: button.setText(str(count.new_click())))
# # button.clicked.connect(partial(button_pressed, count))


central_widget = QWidget()
button_1 = QPushButton('1st Button', central_widget)
button_2 = QPushButton('2nd Button', central_widget)


# Main windows work only if a central widget is defined in them.
win.setCentralWidget(central_widget)
win.show()


# app.exec_() generates the infinite loop for the GUI to run
app.exit(app.exec_())
