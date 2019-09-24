import threading
import time
from abc import abstractmethod, ABCMeta

import numpy as np


class GraphicModule(metaclass=ABCMeta):

    def __init__(self, update_feq: int = 1,
                 only_manual_draw: bool = False) -> None:
        self._update_feq = 1 / update_feq
        self._feq_draw = not only_manual_draw

        self._base_vector = None
        self._main_thread = None

        self._run = True
        self._sig_force_draw = False

    def init_ui(self, base_vector) -> None:
        self._base_vector = base_vector
        self._init_ui_components()

        self._main_thread = self._build_task()
        self._main_thread.start()

    def update_game_vector(self, new_vector: np.ndarray) -> None:
        self._base_vector = new_vector

    def manual_draw(self) -> None:
        self._sig_force_draw = True

    def kill(self):
        self._run = False

    def _main_loop(self) -> None:
        prv_time = time.time()
        while self._run:
            if self._feq_draw and time.time() - prv_time > self._update_feq:
                prv_time = time.time()
                self._draw()
            elif self._sig_force_draw:
                self._sig_force_draw = False
                self._draw()

    def _build_task(self) -> threading.Thread:
        task = threading.Thread(target=self._main_loop, args=[])
        task.daemon = True
        return task

    @abstractmethod
    def _init_ui_components(self) -> None:
        pass

    @abstractmethod
    def _draw(self) -> None:
        pass
