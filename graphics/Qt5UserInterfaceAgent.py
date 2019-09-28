from typing import Callable

import numpy as np
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QDesktopWidget, QWidget, QMainWindow

from abalone import AbaloneModel
from graphics.GraphicModule import _SyncModule


class Qt5UserInterfaceAgent(QMainWindow):

    def __init__(self,
                 sync_module: _SyncModule,
                 disable_click_interface: bool,
                 event_handler: Callable[[QEvent], bool],
                 fps: int,
                 block_size: int = 50,
                 boarder_size: int = 50):
        # noinspection PyArgumentList
        super(Qt5UserInterfaceAgent, self).__init__()
        self.sync_module = sync_module
        self.edge_size = sync_module.base_vector[0]

        self.disable_click_interface = disable_click_interface
        self.event_handler = event_handler

        self.black_size = block_size
        self.boarder_size = boarder_size
        self.fps = fps

        self.init_ui((self.edge_size * 2 - 1) * block_size + boarder_size * 2 + 200,
                     (self.edge_size * 2 - 1) * block_size + boarder_size * 2)

    def init_ui(self, width: int, height: int) -> None:
        self.resize(width, height)
        # noinspection PyArgumentList
        self.setCentralWidget(QWidget())
        self.center()

        self.setWindowTitle("AbaloneRL PyQt5 Graphic User Interface")
        self.build_layout()

        self.show()

    def center(self) -> None:
        qr = self.frameGeometry()
        qr.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(qr.topLeft())

    def build_layout(self) -> None:
        for idx, y, x in AbaloneModel.pos_iterator(self.edge_size):
            pass

    def update_board(self, game_vector: np.ndarray) -> None:
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

    def event(self, q_event):
        return self.event_handler(q_event)
