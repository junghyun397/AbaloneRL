import unittest

import numpy as np

from abalone import AbaloneModel, FieldTemplate

model3 = AbaloneModel.AbaloneAgent(edge_size=3, vector=FieldTemplate.get_basic_start(edge_size=3))
model5 = AbaloneModel.AbaloneAgent(edge_size=5, vector=FieldTemplate.get_basic_start(edge_size=5))
model10 = AbaloneModel.AbaloneAgent(edge_size=10, vector=FieldTemplate.get_basic_start(edge_size=10))


class TestAbaloneIO(unittest.TestCase):

    def test_text_graphic(self):
        print(FieldTemplate.get_text_board(model3.game_vector), "\n")
        print(FieldTemplate.get_text_board(model5.game_vector), "\n")
        print(FieldTemplate.get_text_board(model10.game_vector)), "\n"

    def test_load_model_by_text(self):
        self.assertTrue(np.array_equal(FieldTemplate.load_text_board(
            [3, 0, 0, 0, 0], FieldTemplate.get_text_board(model3.game_vector)), model3.game_vector))
        self.assertTrue(np.array_equal(FieldTemplate.load_text_board(
            [5, 0, 0, 0, 0], FieldTemplate.get_text_board(model5.game_vector)), model5.game_vector))
        self.assertTrue(np.array_equal(FieldTemplate.load_text_board(
            [10, 0, 0, 0, 0], FieldTemplate.get_text_board(model10.game_vector)), model10.game_vector))
