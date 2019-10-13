from multiprocessing import Queue
from typing import Callable

import numpy as np
from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtGui import QColor, QPaintEvent, QPainter, QPen, QBrush, QMouseEvent
from PyQt5.QtWidgets import QDesktopWidget, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout

from abalone import AbaloneModel
from abalone.StoneColor import StoneColor
from graphics.QSyncManager import SyncType, iteration_queue

OUTLINE_COLOR = {
    "NORMAL": QColor("#212121"),
    "SUCCESS_SELECT": QColor("#00C853"),
    "FAIL_SELECT": QColor("#D50000")
}

CELL_COLOR = {StoneColor.BLACK: QColor("#263238"),
              StoneColor.WHITE: QColor("#CFD8DC")}


class _Qt5AbaloneCell(QWidget):

    def __init__(self, block_size: int,
                 click_handler: Callable[[], bool]):
        # noinspection PyArgumentList
        super(_Qt5AbaloneCell, self).__init__()

        self.block_size = block_size
        self.click_handler = click_handler

        self.out_line_size = block_size // 15
        self.cell_color = StoneColor.NONE
        self.selected = False

        self._init_cell()

    def _init_cell(self):
        self.setFixedSize(QSize(self.block_size, self.block_size))
        self.update()

    # Event Handler

    def paintEvent(self, q_paint_event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.cell_color != StoneColor.NONE:
            painter.setBrush(QBrush(CELL_COLOR[self.cell_color], Qt.SolidPattern))

        painter.setPen(QPen(OUTLINE_COLOR["SUCCESS_SELECT"] if self.selected else OUTLINE_COLOR["NORMAL"],
                            self.out_line_size, Qt.SolidLine))
        painter.drawEllipse(self.out_line_size, self.out_line_size,
                            self.block_size - self.out_line_size * 2, self.block_size - self.out_line_size * 2)

    def mouseReleaseEvent(self, q_mouse_event: QMouseEvent):
        if self.click_handler() and q_mouse_event.button() == Qt.LeftButton:
            self.set_select(not self.selected)

    # Cell Control

    def reset_cell(self) -> None:
        self.cell_color = StoneColor.NONE
        self.selected = False
        self.update()

    def set_color(self, color: StoneColor = StoneColor.NONE) -> None:
        if self.cell_color != color:
            self.cell_color = color
            self.update()

    def set_select(self, selected: bool = True) -> None:
        if not (self.cell_color == StoneColor.NONE and not self.selected or self.selected == selected):
            self.selected = selected
            self.update()


class Qt5UserInterfaceAgent(QMainWindow):

    # noinspection PyArgumentList
    def __init__(self,
                 sync_queue: Queue,
                 fps: int = 30,
                 disable_click_interface: bool = True,
                 ui_pipe: Queue = None,
                 block_size: int = 50):
        super(Qt5UserInterfaceAgent, self).__init__()
        self.sync_queue = sync_queue
        self.fps = fps
        self.disable_click_interface = disable_click_interface
        self.ui_pipe = ui_pipe
        self.block_size = block_size

        init_data = sync_queue.get()

        self.edge_size = init_data.game_vector[0]

        self._abalone_cell = list()
        self._timer = None
        self._prv_board_hash = None

        self._wait_ui_response = False

        self._init_ui()
        self.update_board(init_data.game_vector)
        self._init_timer()

    # Init UI

    # noinspection PyArgumentList
    def _init_ui(self) -> None:
        self.setWindowTitle("AbaloneRL Qt5 "
                            + ("Visualizer" if self.disable_click_interface else "Graphic User Interface"))
        self.statusBar().showMessage("AbaloneRL, Ready")

        center_weight = QWidget()
        horizon_layout = QHBoxLayout()

        board_layout = QVBoxLayout()
        board_layout.setSpacing(0)
        board_layout.setContentsMargins(*[self.block_size // 4] * 4)

        self._init_abalone_board(board_layout)

        horizon_layout.addLayout(board_layout)

        center_weight.setLayout(horizon_layout)
        self.setCentralWidget(center_weight)

        qr = self.frameGeometry()
        qr.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(qr.topLeft())

        self.show()

    # noinspection PyArgumentList
    def _init_abalone_board(self, board_layout: QVBoxLayout) -> None:
        # noinspection PyShadowingNames
        def next_layout(y: int):
            new_layout = QHBoxLayout()
            new_layout.setAlignment(Qt.AlignLeft)
            new_layout.addSpacing((self.edge_size - y - 1 if y < self.edge_size else y - self.edge_size + 1)
                                  * (self.block_size + self.block_size // 5) / 2)
            new_layout.setSpacing(self.block_size // 5)
            return new_layout

        prv_layout, prv_y = next_layout(0), 0
        for idx, y, x in AbaloneModel.pos_iterator(self.edge_size):
            if prv_y != y:
                board_layout.addLayout(prv_layout)
                prv_layout, prv_y = next_layout(y), y

            cell = _Qt5AbaloneCell(self.block_size, lambda: True)
            prv_layout.addWidget(cell)
            self._abalone_cell.append(cell)
        board_layout.addLayout(prv_layout)

    # noinspection PyUnresolvedReferences
    def _init_timer(self) -> None:
        self._timer = QTimer()
        self._timer.timeout.connect(self._timer_tick)
        self._timer.start(1000 // self.fps)

    # Qt5 UI

    def update_board(self, game_vector: np.ndarray) -> None:
        self.update_status_bar(game_vector)

        def update(cell, index):
            cell.set_color(StoneColor(game_vector[index + 5]))
            cell.set_select(False)

        self._seq_iteration_board(lambda cell, index: update(cell, index))

    def update_status_bar(self, game_vector: np.ndarray):
        self.statusBar().showMessage("Turns: {0}; Drop Black: {1}; Drop White: {2}; Current Color: {3}"
                                     .format(game_vector[1], game_vector[3], game_vector[4],
                                             "BLACK" if game_vector[2] == StoneColor.BLACK else
                                             ("WHITE" if game_vector[2] == StoneColor.WHITE else "NONE")))

    # Board Control UI

    def reset_board(self) -> None:
        self._iteration_board(lambda cell: cell.reset_cell())

    # Bin Control UI

    def _iteration_board(self, f: Callable[[_Qt5AbaloneCell], None]) -> None:
        for cell in self._abalone_cell:
            f(cell)

    def _seq_iteration_board(self, f: Callable[[_Qt5AbaloneCell, int], None]) -> None:
        for index in range(len(self._abalone_cell)):
            f(self._abalone_cell[index], index)

    def _detect_diff_board(self, game_vector: np.ndarray) -> bool:
        board_hash = hash(game_vector.__str__())
        if self._prv_board_hash == board_hash:
            return False
        else:
            self._prv_board_hash = board_hash
            return True

    # User Click-Interface

    def _timer_tick(self) -> None:
        for queue in iteration_queue(self.sync_queue):
            if queue.sync_type == SyncType.SYNC_DRAW and self._detect_diff_board(queue.game_vector):
                self.update_board(queue.game_vector)
            elif queue.sync_type == SyncType.SYNC_KILL:
                exit()

    def _send_ui_request(self) -> None:
        pass
