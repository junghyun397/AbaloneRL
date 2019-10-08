import random
import sys
import threading
import time
import unittest
from multiprocessing import Process, Queue

from PyQt5.QtWidgets import QApplication

from abalone import FieldTemplate
from graphics.QSyncManager import SyncInit, SyncDraw
from graphics.Qt5UserInterfaceAgent import Qt5UserInterfaceAgent


class TestQt5Graphic(unittest.TestCase):

    def test_visualizer_mode(self):
        board = FieldTemplate.basic_start(5)
        queue = Queue()
        queue.put_nowait(SyncInit(board))

        def update():
            prv_time = time.time()
            while True:
                if prv_time + 1 / 60 < time.time():
                    board[random.randrange(5, board.size)] = random.randrange(0, 3)
                    queue.put_nowait(SyncDraw(board.copy()))
                    prv_time = time.time()

        task = threading.Thread(target=update, args=[])
        task.daemon = True
        task.start()

        app = QApplication(sys.argv)
        ex = Qt5UserInterfaceAgent(queue)
        sys.exit(app.exec())

    def test_in_process(self):
        process = Process(target=self.test_visualizer_mode, args=[])
        process.start()
        process.join()

    def test_in_thread(self):
        thread = threading.Thread(target=self.test_visualizer_mode, args=[])
        thread.start()
