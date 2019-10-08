import multiprocessing
from abc import abstractmethod, ABCMeta
from multiprocessing import Queue

import numpy as np

from graphics.QSyncManager import SyncDraw, SyncKill, SyncInit


class GraphicModule(metaclass=ABCMeta):

    def __init__(self, update_feq: int) -> None:
        self.update_feq = update_feq

        self.base_vector = None

        self.sync_queue = Queue()
        self._graphic_process = None

    def init_ui(self, base_vector: np.ndarray) -> None:
        self.base_vector = base_vector
        self.sync_queue.put_nowait(SyncInit(base_vector))

        self._graphic_process = self._build_process()
        self._graphic_process.start()

    def update_game_vector(self, new_vector: np.ndarray) -> None:
        self.base_vector = new_vector

    def draw(self) -> None:
        self.sync_queue.put_nowait(SyncDraw(self.base_vector.copy()))

    def kill(self) -> None:
        self.sync_queue.put_nowait(SyncKill())

    @abstractmethod
    def _build_process(self) -> multiprocessing.Process:
        pass
