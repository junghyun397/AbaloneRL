import multiprocessing
import os
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from graphics.GraphicModule import GraphicModule
from graphics.qt5.Qt5UserInterfaceAgent import Qt5UserInterfaceAgent


class Qt5Graphic(GraphicModule):

    def __init__(self, update_feq: int = 20,
                 use_rescale: bool = True):
        super().__init__(update_feq)

        self.use_rescale = use_rescale

    def _build_process(self) -> multiprocessing.Process:
        process = multiprocessing.Process(target=self._run_pyqt5_ui, args=())
        process.daemon = True
        process.name = "AbaloneRL Qt5 Graphic-Visualizer"
        return process

    def _run_pyqt5_ui(self) -> None:
        if self.use_rescale:
            os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
            QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

        app = QApplication([])
        _ = self._get_ex()
        sys.exit(app.exec_())

    def _get_ex(self) -> Qt5UserInterfaceAgent:
        return Qt5UserInterfaceAgent(sync_queue=self.sync_queue, fps=self.update_feq)
