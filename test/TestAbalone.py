import unittest

import numpy as np

from abalone import AbaloneModel
from abalone.AbaloneAgent import AbaloneAgent

model3 = AbaloneAgent(edge_size=3)
model5 = AbaloneAgent(edge_size=5)


model3_pos_list = [((0, 0), 0), ((1, 1), 4), ((3, 1), 12)]

model5_pos_list = [((0, 0), 0), ((1, 1), 6), ((5, 1), 35), ((6, 2), 43), ((7, 3), 50), ((7, 5), 52), ((8, 4), 56)]


class TestAbalone(unittest.TestCase):

    def test_2d_2_1d_pos(self):
        # Model 3
        for n in model3_pos_list:
            self.assertEqual(model3.get_1d_pos(n[0]), n[1])

        # Model 5
        for n in model5_pos_list:
            self.assertEqual(model5.get_1d_pos(n[0]), n[1])

    def test_valid_pos(self):
        # Model 3
        self.assertTrue(model3.check_valid_pos(0, 0))
        self.assertTrue(model3.check_valid_pos(1, 3))
        self.assertTrue(model3.check_valid_pos(2, 4))

        self.assertFalse(model3.check_valid_pos(3, 0))
        self.assertFalse(model3.check_valid_pos(4, 1))
        self.assertFalse(model3.check_valid_pos(5, 1))
        self.assertFalse(model3.check_valid_pos(4, 5))

        # Model 5
        self.assertTrue(model5.check_valid_pos(0, 0))
        self.assertTrue(model5.check_valid_pos(2, 6))
        self.assertTrue(model5.check_valid_pos(4, 8))
        self.assertTrue(model5.check_valid_pos(5, 8))

        self.assertFalse(model5.check_valid_pos(5, 0))
        self.assertFalse(model5.check_valid_pos(6, 1))
        self.assertFalse(model5.check_valid_pos(8, 3))

    def test_1d_2_2d_pos(self):
        # Model 3
        for n in model3_pos_list:
            self.assertEqual(model3.get_2d_pos(n[1]), n[0])

        # Model 5
        for n in model5_pos_list:
            self.assertEqual(model5.get_2d_pos(n[1]), n[0])

    def test_to_vector(self):
        self.assertTrue(np.equal(model3.game_vector, np.array([0] * (model3.field_size + 5))))
        self.assertTrue(np.equal(model5.game_vector, np.array([0] * (model5.field_size + 5))))

    def field_size_2_edge_size(self):
        self.assertTrue(AbaloneModel.get_edge_size(model3.field_size), model3.edge_size)
        self.assertTrue(AbaloneModel.get_edge_size(model5.field_size), model5.edge_size)

    def test_can_push_stone(self):
        pass

    def test_push_stone(self):
        pass

    def test_end_game(self):
        pass
