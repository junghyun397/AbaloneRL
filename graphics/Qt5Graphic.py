import sys
import threading
from typing import Callable

import numpy as np
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QWidget
from qtconsole.qt import QtGui

from abalone import AbaloneModel
from abalone.HexDescription import HexDescription
from graphics.GraphicModule import GraphicModule, SyncModule


class _Qt5GraphicWindowAgent(QMainWindow):

    def __init__(self,
                 sync_module: SyncModule,
                 event_handler: Callable[[QEvent], bool],
                 fps: int,
                 block_size: int = 50,
                 boarder_size: int = 50):
        super(_Qt5GraphicWindowAgent, self).__init__()
        self.sync_module = sync_module

        self.edge_size = sync_module.base_vector[0]
        self.event_handler = event_handler

        self.black_size = block_size
        self.boarder_size = boarder_size
        self.fps = fps

        self.init_ui((self.edge_size * 2 - 1) * block_size + boarder_size * 2 + 200,
                     (self.edge_size * 2 - 1) * block_size + boarder_size * 2)

    def init_ui(self, width: int, height: int) -> None:
        self.resize(width, height)
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

    def event(self, q_event):
        return self.event_handler(q_event)


class Qt5Graphic(GraphicModule):

    def __init__(self, update_feq: int = 120,
                 only_manual_draw: bool = False,
                 use_click_interface: bool = False,
                 event_handler: Callable[[int, int, HexDescription], bool] = (lambda _, __, ___: True)):
        super().__init__(update_feq, only_manual_draw)
        self.event_handler = event_handler
        self.n_agent = None

        if not use_click_interface:
            self.process_event = (lambda _: True)

    def process_event(self, q_event: QEvent) -> bool:
        x, y, des = self.n_agent.decode_action(0)
        return self.event_handler(x, y, des)

    def _build_task(self) -> threading.Thread:
        task = threading.Thread(target=self.__run_pyqt5_ui, args=[])
        task.daemon = True
        return task

    def __run_pyqt5_ui(self) -> None:
        app = QtGui.QApplication(sys.argv)
        ex = _Qt5GraphicWindowAgent(self.sync_module, self.process_event, self.update_feq)
        sys.exit(app.exec_())
