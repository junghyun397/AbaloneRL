import threading
from abc import abstractmethod, ABCMeta
from queue import Queue

import numpy as np

from graphics.QSyncManager import SyncBoard, SyncDraw, SyncKill, SyncInit


class GraphicModule(metaclass=ABCMeta):

    def __init__(self, update_feq: int,
                 disable_auto_draw: bool) -> None:
        self.update_feq = update_feq
        self.feq_draw = not disable_auto_draw

        self.base_vector = None

        self.sync_queue = Queue()
        self._main_thread = None

    def init_ui(self, base_vector: np.ndarray) -> None:
        self.base_vector = base_vector
        self.sync_queue.put(SyncInit(base_vector))

        self._main_thread = self._build_task()
        self._main_thread.start()

    def update_game_vector(self, new_vector: np.ndarray) -> None:
        self.base_vector = new_vector
        self.sync_queue.put(SyncBoard(new_vector))

    def manual_draw(self) -> None:
        self.sync_queue.put(SyncDraw(self.base_vector))

    def kill(self) -> None:
        self.sync_queue.put(SyncKill())

    @abstractmethod
    def _build_task(self) -> threading.Thread:
        pass
