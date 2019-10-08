import os
import sys
import threading

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from graphics.GraphicModule import GraphicModule
from graphics.Qt5UserInterfaceAgent import Qt5UserInterfaceAgent


class Qt5Graphic(GraphicModule):

    def __init__(self, update_feq: int = 20,
                 disable_auto_draw: bool = False,
                 use_rescale: bool = True):
        super().__init__(update_feq, disable_auto_draw)

        self.use_rescale = use_rescale

    def _build_task(self) -> threading.Thread:
        task = threading.Thread(target=self._run_pyqt5_ui, args=[])
        task.daemon = True
        return task

    def _run_pyqt5_ui(self) -> None:
        if self.use_rescale:
            os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
            QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

        app = QApplication([])
        ex = self._get_ex()
        sys.exit(app.exec_())

    def _get_ex(self) -> Qt5UserInterfaceAgent:
        return Qt5UserInterfaceAgent(sync_queue=self.sync_queue, fps=self.update_feq,
                                     disable_click_interface=True, click_handler=lambda _: False)
