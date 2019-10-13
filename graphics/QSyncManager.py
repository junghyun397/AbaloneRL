import queue
from enum import Enum
from typing import Iterator

import numpy as np


class SyncType(Enum):
    SYNC_INIT = 0
    SYNC_BOARD = 1
    SYNC_DRAW = 2
    SYNC_KILL = 3

    SYNC_EVENT = 4


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


class SyncUIEvent(SyncModule):

    def __init__(self):
        super().__init__(SyncType.SYNC_EVENT)


def iteration_queue(target_queue) -> Iterator[SyncModule]:
    while True:
        try:
            yield target_queue.get_nowait()
        except queue.Empty:
            break
