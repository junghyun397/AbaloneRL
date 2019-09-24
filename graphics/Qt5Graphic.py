from typing import Callable

import numpy as np
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QWidget

from abalone import AbaloneModel
from abalone.HexDescription import HexDescription
from graphics.GraphicModule import GraphicModule


class _Qt5GraphicWindowAgent(QMainWindow):

    def __init__(self,
                 edge_size: int,
                 event_handler: Callable[[QEvent], bool],
                 block_size: int = 100,
                 boarder_size: int = 100,
                 fps: int = 120):
        super(_Qt5GraphicWindowAgent, self).__init__(flags=0)
        self.edge_size = edge_size
        self.event_handler = event_handler
        self.black_size = block_size
        self.boarder_size = boarder_size
        self.fps = fps

        self.init_ui((edge_size * 2 - 1) * block_size + boarder_size * 2 + 200,
                     (edge_size * 2 - 1) * block_size + boarder_size * 2)

    def init_ui(self, width: int, height: int) -> None:
        self.resize(width, height)
        self.setCentralWidget(QWidget(flags=0))
        self.center()

        self.setWindowTitle("AbaloneRL PyQt5 User Interface")
        self.build_layout()

        self.show()

    def center(self) -> None:
        qr = self.frameGeometry()
        qr.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(qr.topLeft())

    def build_layout(self) -> None:
        for y, x in AbaloneModel.pos_iterator(self.edge_size):
            pass

    def update_board(self, game_vector: np.ndarray) -> None:
        self._clear_cell()
        self._draw_guid_line()
        self._draw_cell(game_vector)
        self._draw_info(game_vector)

    def _draw_guid_text(self) -> None:
        pass

    def _draw_guid_line(self) -> None:
        pass

    def _draw_cell(self, game_vector: np.ndarray) -> None:
        pass

    def _draw_info(self, game_vector: np.ndarray) -> None:
        pass

    def _update_cell(self) -> None:
        pass

    def event(self, qEvent):
        self.event_handler(qEvent)


class Qt5Graphic(GraphicModule):

    def __init__(self, update_feq: int = 120,
                 only_manual_draw: bool = False,
                 use_click_interface: bool = False,
                 event_handler: Callable[[int, int, HexDescription], bool] = (lambda _, __, ___: False)):
        super().__init__(update_feq, only_manual_draw)
        self.event_handler = event_handler
        self.n_agent = None

        if not use_click_interface:
            self.process_event = (lambda _, __: True)

    def process_event(self, qEvent: QEvent) -> bool:
        x, y, des = self.n_agent.decode_action(0)
        return self.event_handler(x, y, des)

    def _init_ui_components(self) -> None:
        pass

    def _draw(self) -> None:
        pass
