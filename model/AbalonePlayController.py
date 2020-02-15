from multiprocessing.queues import Queue

from abalone.AbaloneModel import AbaloneAgent
from abalone.HexDescription import HexDescription
from graphics.QSyncManager import SyncSelect


class AbalonePlayController:

    def __init__(self, abalone_model: AbaloneAgent, sync_queue: Queue):
        self.abalone_model = abalone_model
        self.sync_queue = sync_queue

        self._select_mode = True
        self._selected = list()

    def click_stone_event(self, y: int, x: int) -> None:
        if self._select_mode:
            if self.abalone_model.can_select_stone([(y, x)]):
                return

            if not (y, x) in self._selected:
                self._select_stone(y, x)
            else:
                self._selected.remove((y, x))
                self.sync_queue.put_nowait(SyncSelect(False, y, x))
        else:
            if not self.abalone_model.can_select_stone(self._selected) or \
                    not self.abalone_model.can_push_stone(self._selected[0][0], self._selected[0][1], HexDescription.X):
                return

    def _select_stone(self, y: int, x: int):
        self._selected.append((y, x))
        self.sync_queue.put_nowait(SyncSelect(True, y, x))

    def _unselect_stone(self, all_stone: bool = False, y: int = None, x: int = None):
        if all_stone:
            for y, x in self._selected:
                self._unselect_stone(y=y, x=x)

        self._selected.remove((y, x))
        self.sync_queue.put_nowait(SyncSelect(False, y, x))

    def enter_event(self):
        self._select_mode = not self._select_mode

    def _push_stone(self):
        pass
