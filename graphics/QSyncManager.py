from enum import Enum
from queue import Queue
from typing import Iterator

import numpy as np


class SyncType(Enum):
    SYNC_INIT = 0
    SYNC_BOARD = 1
    SYNC_DRAW = 2
    SYNC_KILL = 3


class SyncModule:

    def __init__(self, sync_type: SyncType):
        self.sync_type = sync_type
        self.game_vector = None


class SyncBoard(SyncModule):

    def __init__(self, game_vector: np.ndarray):
        super().__init__(SyncType.SYNC_BOARD)

        self.game_vector = game_vector


class SyncInit(SyncBoard):

    def __init__(self, game_vector: np.ndarray):
        super().__init__(game_vector)
        self.sync_type = SyncType.SYNC_INIT


class SyncDraw(SyncBoard):

    def __init__(self, game_vector: np.ndarray):
        super().__init__(game_vector)
        self.sync_type = SyncType.SYNC_DRAW


class SyncKill(SyncModule):

    def __init__(self):
        super().__init__(SyncType.SYNC_KILL)


def iteration_queue(queue: Queue[SyncModule]) -> Iterator[SyncModule]:
    while True:
        rq = queue.get()
        if rq is not None:
            yield rq
        else:
            break
