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


def openCamera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('Frame', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyWindow('Frame')
    return



app = QApplication([])
win = QMainWindow()

# count = ClickCount(0)

# button = QPushButton(str(count.get_count()))
# button.clicked.connect(lambda _: button.setText(str(count.new_click())))
# # button.clicked.connect(partial(button_pressed, count))


central_widget = QWidget()
layout = QVBoxLayout(central_widget)

count_1 = ClickCount()
button_1 = QPushButton(str(count_1.get_count()), central_widget)
# button_1.setGeometry(0, 0, 120, 40)
button_1.clicked.connect(lambda _: button_1.setText(str(count_1.new_click())))

count_2 = ClickCount()
button_2 = QPushButton('2nd Button', central_widget)
# button_2.setGeometry(0, 50, 120, 40)


from random import randint
button_2.clicked.connect(lambda _: button_2.setStyleSheet(
    "background-color: rgb({}, {}, {})".format(randint(0, 255), randint(0, 255), randint(0, 255))
    ))


button_3 = QPushButton('Camera', central_widget)
button_3.clicked.connect(openCamera)


layout.addWidget(button_1)
layout.addWidget(button_2)
layout.addWidget(button_3)

# Main windows work only if a central widget is defined in them.
win.setCentralWidget(central_widget)
win.show()


# app.exec_() generates the infinite loop for the GUI to run
app.exit(app.exec_())
