import threading
from abc import abstractmethod, ABCMeta

import numpy as np


class _SyncModule:

    def __init__(self):
        self.base_vector = None
        self.run = True

        self.sig_force_draw = False


class GraphicModule(metaclass=ABCMeta):

    def __init__(self, update_feq: int,
                 disable_auto_draw: bool) -> None:
        self.update_feq = update_feq
        self.feq_draw = not disable_auto_draw

        self.sync_module = _SyncModule()

        self._main_thread = None

    def init_ui(self, base_vector) -> None:
        self.sync_module.base_vector = base_vector

        self._main_thread = self._build_task()
        self._main_thread.start()

    def update_game_vector(self, new_vector: np.ndarray) -> None:
        self.sync_module.base_vector = new_vector

    def manual_draw(self) -> None:
        self.sync_module.sig_force_draw = True

    def kill(self) -> None:
        self.sync_module.run = False

    @abstractmethod
    def _build_task(self) -> threading.Thread:
        pass
