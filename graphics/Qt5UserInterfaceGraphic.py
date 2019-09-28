import sys
import threading
from typing import Callable

from PyQt5.QtCore import QEvent
from qtconsole.qt import QtGui

from graphics.GraphicModule import GraphicModule
from graphics.Qt5UserInterfaceAgent import Qt5UserInterfaceAgent


class Qt5UserInterfaceGraphic(GraphicModule):

    def __init__(self, user_control_interface: Callable[[int], bool],
                 update_feq: int = 60):
        super().__init__(update_feq, False)

        self.control_interface = user_control_interface

    def _build_task(self) -> threading.Thread:
        task = threading.Thread(target=self._run_pyqt5_ui, args=[])
        task.daemon = True
        return task

    def _run_pyqt5_ui(self) -> None:
        app = QtGui.QApplication(sys.argv)
        Qt5UserInterfaceAgent(sync_module=self.sync_module,
                              disable_click_interface=True, event_handler=self._process_event,
                              fps=self.update_feq)
        sys.exit(app.exec_())

    def _process_event(self, q_event: QEvent) -> bool:
        return self.control_interface(1)
