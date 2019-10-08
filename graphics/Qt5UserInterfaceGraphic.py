from graphics.Qt5Graphic import Qt5Graphic
from graphics.Qt5UserInterfaceAgent import Qt5UserInterfaceAgent


class Qt5UserInterfaceGraphic(Qt5Graphic):

    def __init__(self, update_feq: int = 60):
        super().__init__(update_feq, False)

    def _get_ex(self) -> Qt5UserInterfaceAgent:
        return Qt5UserInterfaceAgent(sync_queue=self.sync_queue,
                                     disable_click_interface=False, click_handler=self._process_event,
                                     fps=self.update_feq)

    def _process_event(self, x: int, y: int) -> bool:
        return True
