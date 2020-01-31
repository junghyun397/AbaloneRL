from multiprocessing import Queue
from typing import Callable

from graphics.QSyncManager import SyncUIEvent, iteration_queue
from graphics.qt5.Qt5Graphic import Qt5Graphic
from graphics.qt5.Qt5UserInterfaceAgent import Qt5UserInterfaceAgent


class Qt5PlayableGraphic(Qt5Graphic):

    def __init__(self, update_feq: int = 20,
                 use_rescale: bool = True,
                 event_iter_feq: int = 60,
                 event_handler: Callable[[SyncUIEvent], bool] = lambda _: False):
        super().__init__(update_feq, use_rescale)

        self.event_handler = event_handler

        self.handler_queue = Queue()

    def _get_ex(self) -> Qt5UserInterfaceAgent:
        return Qt5UserInterfaceAgent(sync_queue=self.sync_queue, fps=self.update_feq,
                                     disable_click_interface=False, ui_pipe=self.handler_queue)

    def iter_event(self) -> None:
        for event in iteration_queue(self.handler_queue):
            pass
