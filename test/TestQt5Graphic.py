import random
import sys
import threading
import time
import unittest
from multiprocessing import Process

from PyQt5.QtWidgets import QApplication

from abalone import FieldTemplate
from graphics.GraphicModule import SyncModule
from graphics.Qt5UserInterfaceAgent import Qt5UserInterfaceAgent


class TestQt5Graphic(unittest.TestCase):

    def test_visualizer_mode(self):
        board = FieldTemplate.basic_start(5)

        def update():
            prv_time = time.time()
            while True:
                if prv_time + 1 / 60 < time.time():
                    board[random.randrange(5, board.size)] = random.randrange(0, 3)
                    prv_time = time.time()

        task = threading.Thread(target=update, args=[])
        task.daemon = True
        task.start()

        app = QApplication(sys.argv)
        ex = Qt5UserInterfaceAgent(SyncModule(board), disable_auto_draw=False)
        sys.exit(app.exec())

    def test_ui_mode(self):
        board = FieldTemplate.basic_start(5)

        app = QApplication(sys.argv)
        ex = Qt5UserInterfaceAgent(SyncModule(board), disable_click_interface=False, click_handler=lambda _, __: True)
        sys.exit(app.exec())

    def test_in_process(self):
        process = Process(target=self.test_ui_mode, args=[])
        process.start()
        process.join()

    def test_in_thread(self):
        thread = threading.Thread(target=self.test_ui_mode, args=[])
        thread.start()
