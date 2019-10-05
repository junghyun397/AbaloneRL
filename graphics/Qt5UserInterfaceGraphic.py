from typing import Callable

from PyQt5.QtCore import QEvent

from graphics.Qt5Graphic import Qt5Graphic
from graphics.Qt5UserInterfaceAgent import Qt5UserInterfaceAgent


class Qt5UserInterfaceGraphic(Qt5Graphic):

    def __init__(self, user_control_interface: Callable[[int], bool],
                 update_feq: int = 60):
        super().__init__(update_feq, False)

        self.control_interface = user_control_interface

    def _get_ex(self) -> Qt5UserInterfaceAgent:
        return Qt5UserInterfaceAgent(sync_module=self.sync_module,
                              disable_click_interface=False, event_handler=self._process_event,
                              fps=self.update_feq)

    def _process_event(self, q_event: QEvent) -> bool:
        return self.control_interface(1)
