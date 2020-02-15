import queue
from enum import Enum
from multiprocessing import Queue
from typing import Iterator

import numpy as np


class SyncType(Enum):
    SYNC_INIT = 0
    SYNC_BOARD = 1
    SYNC_DRAW = 2
    SYNC_KILL = 3

    SYNC_CLICK = 4
    SYNC_ENTER = 5
    SYNC_SELECT = 6


class SyncData:

    def __init__(self, sync_type: SyncType):
        self.sync_type = sync_type


class SyncBoard(SyncData):

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


class SyncKill(SyncData):

    def __init__(self):
        super().__init__(SyncType.SYNC_KILL)


class SyncClick(SyncData):

    def __init__(self, y: int, x: int):
        super().__init__(SyncType.SYNC_CLICK)
        self.y, self.x = y, x


class SyncEnter(SyncData):

    def __init__(self):
        super().__init__(SyncType.SYNC_ENTER)


class SyncSelect(SyncData):

    def __init__(self, selected: bool, y: int, x: int):
        super().__init__(SyncType.SYNC_SELECT)
        self.selected = selected
        self.y, self.x = y, x


def iteration_queue(target_queue: Queue) -> Iterator:
    while True:
        try:
            yield target_queue.get_nowait()
        except queue.Empty:
            break
