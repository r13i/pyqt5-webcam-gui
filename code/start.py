import logging
from PyQt5.QtWidgets import QApplication

from models import Camera
from views import StartWindow

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s')
    logger = logging.getLogger()

    camera = Camera(0)
    camera.initialize()
    logger.info("Initialized: {}".format(camera))

    app = QApplication([])
    logger.info("Starting main window ...")
    start_window = StartWindow(camera, logger)
    start_window.show()

    app.exit(app.exec_())
