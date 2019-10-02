from typing import Callable

import numpy as np
from PyQt5.QtCore import QEvent, QSize, Qt
from PyQt5.QtGui import QColor, QPaintEvent, QPainter, QPen, QBrush, QMouseEvent
from PyQt5.QtWidgets import QDesktopWidget, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout

from abalone import AbaloneModel
from abalone.StoneColor import StoneColor
from graphics.GraphicModule import SyncModule

BACKGROUND_COLOR = QColor("#FFFFFF")

BOUND_COLOR = QColor("#000000")
SELECTED_BOUND_COLOR = QColor("#777777")

CELL_COLOR = {StoneColor.NONE: QColor("#111111"),
              StoneColor.BLACK: QColor("#222222"),
              StoneColor.WHITE: QColor("#333333")}


class _Qt5AbaloneCell(QWidget):

    def __init__(self, y: int, x: int, block_size: int):
        # noinspection PyArgumentList
        super(_Qt5AbaloneCell, self).__init__()

        self.y, self.x = y, x
        self.block_size = block_size
        self.out_line_size = block_size // 15

        self.stone_color = StoneColor.NONE
        self.selected = False

        self.init_cell()

    def init_cell(self):
        self.setFixedSize(QSize(self.block_size, self.block_size))
        self.update()

    # Event Handler

    def paintEvent(self, q_paint_event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.stone_color != StoneColor.NONE:
            painter.setBrush(QBrush(CELL_COLOR[self.stone_color], Qt.SolidPattern))

        painter.setPen(QPen(SELECTED_BOUND_COLOR if self.selected else BOUND_COLOR,
                            self.out_line_size, Qt.SolidLine))
        painter.drawEllipse(self.out_line_size, self.out_line_size,
                            self.block_size - self.out_line_size * 2, self.block_size - self.out_line_size * 2)

    def mouseReleaseEvent(self, q_mouse_event: QMouseEvent):
        if q_mouse_event.button() == Qt.LeftButton and not self.selected:
            self.set_select(True)
        elif q_mouse_event.button() == Qt.RightButton and self.selected:
            self.set_select(False)

    # Cell Control

    def reset_cell(self) -> None:
        self.stone_color = StoneColor.NONE
        self.selected = False
        self.update()

    def set_color(self, color: StoneColor = StoneColor.NONE) -> None:
        self.stone_color = color
        self.update()

    def set_select(self, selected: bool = True) -> None:
        self.selected = selected
        self.update()


class Qt5UserInterfaceAgent(QMainWindow):

    def __init__(self,
                 sync_module: SyncModule,
                 fps: int,
                 disable_click_interface: bool,
                 event_handler: Callable[[QEvent], bool],
                 block_size: int = 50,
                 boarder_size: int = 50):
        # noinspection PyArgumentList
        super(Qt5UserInterfaceAgent, self).__init__()
        self.sync_module = sync_module
        self.fps = fps

        self.disable_click_interface = disable_click_interface
        self.event_handler = event_handler

        self.edge_size = sync_module.base_vector[0]

        self.block_size = block_size
        self.boarder_size = boarder_size

        self._prv_board_hash = None

        self.init_ui()
        self.init_timer(fps)

    # Init UI

    # noinspection PyArgumentList
    def init_ui(self) -> None:
        self.setWindowTitle("AbaloneRL PyQt5 Graphic User Interface")

        center_weight = QWidget()
        horizon_layout = QHBoxLayout()

        board_layout = QVBoxLayout()
        self.init_abalone_board(board_layout)

        horizon_layout.addLayout(board_layout)

        center_weight.setLayout(horizon_layout)
        self.setCentralWidget(center_weight)
        self.center()

        self.show()

    # noinspection PyArgumentList
    def init_abalone_board(self, board_layout: QVBoxLayout) -> None:
        offset = 0

        def build_layout():
            new_layout = QHBoxLayout()
            new_layout.setAlignment(Qt.AlignLeft)
            new_layout.addSpacing(offset)
            return new_layout

        prv_layout, prv_y = build_layout(), 0
        for idx, y, x in AbaloneModel.pos_iterator(self.edge_size):
            if prv_y != y:
                board_layout.addLayout(prv_layout)
                prv_layout, prv_y = build_layout(), y

            cell = _Qt5AbaloneCell(y, x, self.block_size)
            prv_layout.addWidget(cell)
        board_layout.addLayout(prv_layout)

    def init_timer(self, feq: int) -> None:
        pass

    # Qt5 UI

    def center(self) -> None:
        qr = self.frameGeometry()
        qr.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(qr.topLeft())

    # Control UI

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

    # Bin Control UI

    def _detect_diff_board(self) -> bool:
        board_hash = self.sync_module.base_vector.__hash__
        if self._prv_board_hash == board_hash:
            return False
        else:
            self._prv_board_hash = board_hash
            return True

    # User Click-Interface

    # def event(self, q_event):
    #     return self.event_handler(q_event)
