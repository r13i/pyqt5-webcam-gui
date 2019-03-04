import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


cap = cv2.VideoCapture(0)
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



app = QApplication([])
win = QMainWindow()

button = QPushButton('MyButton')

# Main windows work only if a central widget is defined in them.
win.setCentralWidget(button)
win.show()


# app.exec_() generates the infinite loop for the GUI to run
app.exit(app.exec_())