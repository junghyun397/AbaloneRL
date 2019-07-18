import numpy as np
from PyQt5.QtWidgets import QWidget, QDesktopWidget

from graphics.GraphicModule import GraphicModule


class ThreadAdapter:
    pass


class Qt5GraphicWindowAdapter(QWidget):

    def __init__(self, edge_size: int, block_size: int = 100):
        super().__init__()
        self.edge_size = edge_size
        self.init_ui(edge_size * 2 * block_size, edge_size * 2 * block_size)

    def init_ui(self, width: int, height: int) -> None:
        self.resize(width, height)
        self.center()
        self.setWindowTitle("AbaloneRL User Interface")
        self.show()

    def center(self) -> None:
        qr = self.frameGeometry()
        qr.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(qr.topLeft())

    def draw(self, game_vector: np.ndarray) -> None:
        pass


class Qt5Graphic(GraphicModule):

    def __init__(self):
        super().__init__()

    def get_click_interface(self) -> None:
        pass

    def draw(self) -> None:
        pass
