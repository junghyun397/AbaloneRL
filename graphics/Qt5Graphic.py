import sys
import threading

from qtconsole.qt import QtGui

from graphics.GraphicModule import GraphicModule
from graphics.Qt5UserInterfaceAgent import Qt5UserInterfaceAgent


class Qt5Graphic(GraphicModule):

    def __init__(self, update_feq: int = 20,
                 only_manual_draw: bool = False):
        super().__init__(update_feq, only_manual_draw)

    def _build_task(self) -> threading.Thread:
        task = threading.Thread(target=self._run_pyqt5_ui, args=[])
        task.daemon = True
        return task

    def _run_pyqt5_ui(self) -> None:
        app = QtGui.QApplication(sys.argv)
        # noinspection PyUnusedLocal
        ex = Qt5UserInterfaceAgent(sync_module=self.sync_module,
                              disable_click_interface=True, event_handler=lambda _: False,
                              fps=self.update_feq)
        sys.exit(app.exec_())
