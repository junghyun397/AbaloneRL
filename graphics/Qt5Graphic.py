import sys
import threading

import numpy as np
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget

from graphics.GraphicModule import GraphicModule


class Qt5GraphicWindowAdapter(QWidget):

    # noinspection PyArgumentList
    def __init__(self, width: int, height: int):
        super().__init__()
        self.init_ui(width, height)

    def init_ui(self, width: int, height: int) -> None:
        self.resize(width, height)
        self.center()
        self.setWindowTitle("AbaloneRL User Interface")
        self.show()

    def center(self) -> None:
        qr = self.frameGeometry()
        qr.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(qr.topLeft())

    def draw(self) -> None:
        pass


class Qt5Graphic(GraphicModule):

    def __init__(self, base_vector: np.ndarray):
        super().__init__(base_vector)

        def run():
            app = QApplication(sys.argv)
            q_window = Qt5GraphicWindowAdapter(1920, 1080)
            app.exec_()

        thread = threading.Thread(target=run)
        thread.daemon = True
        thread.start()

    def get_click_interface(self) -> None:
        pass

    def draw(self) -> None:
        pass