import random
import sys
import threading
import time
import unittest
from multiprocessing import Process, Queue
from typing import Callable

from PyQt5.QtWidgets import QApplication

from abalone import FieldTemplate
from graphics.QSyncManager import SyncInit, SyncDraw
from graphics.Qt5UserInterfaceAgent import Qt5UserInterfaceAgent


def random_shift_worker(edge_size: int = 5, fps: int = 60, shift: int = 20) -> Callable[[], None]:
    board = FieldTemplate.basic_start(edge_size)
    queue = Queue()
    queue.put_nowait(SyncInit(board))

    def update():
        prv_time = time.time()
        while True:
            if prv_time + 1 / fps < time.time():
                for _ in range(0, shift):
                    board[random.randrange(5, board.size)] = random.randrange(0, 3)
                queue.put_nowait(SyncDraw(board.copy()))
                prv_time = time.time()

    task = threading.Thread(target=update, args=[])
    task.daemon = True
    task.start()

    # noinspection PyUnusedLocal
    def run_ui():
        app = QApplication(sys.argv)
        ex = Qt5UserInterfaceAgent(queue)
        sys.exit(app.exec())

    return run_ui


class TestQt5Graphic(unittest.TestCase):

    def test_in_process(self):
        process = Process(target=random_shift_worker(), args=[])
        process.start()
        process.join()

    def test_in_thread(self):
        thread = threading.Thread(target=random_shift_worker(), args=[])
        thread.start()
        thread.join()
