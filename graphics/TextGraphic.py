import threading
import time

import numpy as np

from abalone import FieldTemplate
from graphics.GraphicModule import GraphicModule
from graphics.QSyncManager import iteration_queue, SyncType


class TextGraphic(GraphicModule):

    def __init__(self, update_feq: int = 1,
                 disable_auto_draw: bool = False,
                 use_info_text: bool = True):
        super().__init__(update_feq, disable_auto_draw)

        self._info_text = ">> Turns: {0}, Dropped black: {1}, Dropped white: {2}\n" if use_info_text else None
        self._draw = self._initialized_draw

    def _build_task(self) -> threading.Thread:
        task = threading.Thread(target=self._main_loop, args=[])
        task.daemon = True
        return task

    def _main_loop(self) -> None:
        prv_time, run = time.time(), True
        while run:
            if time.time() - prv_time > 1 / self.update_feq:
                for queue in iteration_queue(self.sync_queue):
                    if queue.sync_type == SyncType.SYNC_DRAW:
                        self._draw(queue.game_vector)
                    elif self.feq_draw and queue.sync_type == SyncType.SYNC_BOARD:
                        self._draw(queue.game_vector)
                    elif queue.sync_type == SyncType.SYNC_KILL:
                        run = False
                        break
                prv_time = time.time()

    def _draw(self, game_vector: np.ndarray) -> None:
        pass

    def _initialized_draw(self, game_vector: np.ndarray) -> None:
        print(FieldTemplate.get_text_board(game_vector), "\n", self._info_text.format(
            game_vector[1], game_vector[3], game_vector[4]))
