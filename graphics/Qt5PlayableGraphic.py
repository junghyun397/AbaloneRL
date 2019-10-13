from multiprocessing import Queue

from graphics.Qt5Graphic import Qt5Graphic
from graphics.Qt5UserInterfaceAgent import Qt5UserInterfaceAgent


class Qt5PlayableGraphic(Qt5Graphic):

    def __init__(self, update_feq: int = 20,
                 use_rescale: bool = True):
        super().__init__(update_feq, use_rescale)

        self.handler_queue = Queue()

    def _get_ex(self) -> Qt5UserInterfaceAgent:
        return Qt5UserInterfaceAgent(sync_queue=self.sync_queue, fps=self.update_feq,
                                     disable_click_interface=False, ui_pipe=self.handler_queue)
