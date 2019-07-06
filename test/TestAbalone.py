import unittest

import numpy as np

from abalone import AbaloneModel

model3 = AbaloneModel.AbaloneAgent(edge_size=3)
model5 = AbaloneModel.AbaloneAgent(edge_size=5)

# Convert Pos-Dimension resource
model3_pos_list = [((0, 0), 0), ((1, 1), 4), ((3, 1), 12)]
model5_pos_list = [((0, 0), 0), ((1, 1), 6), ((5, 1), 35), ((6, 2), 43), ((7, 3), 50), ((7, 5), 52), ((8, 4), 56)]

# Pos-Validation resource
model3_validation_pos = [((0, 0), True), ((1, 3), True), ((2, 4), True),
                         ((3, 0), False), ((4, 1), False), ((5, 1), False, ((4, 5), False))]
model5_validation_pos = [((0, 0), True), ((2, 6), True), ((4, 8), True), ((5, 8), True),
                         ((5, 0), False), ((6, 1), False), ((8, 3), False)]


class TestAbalone(unittest.TestCase):

    def test_pos_generator(self):
        for index, y, x in AbaloneModel.pos_generator(3):
            self.assertTrue(index < AbaloneModel.get_field_size(3))
            self.assertEqual(model3.get_1d_pos(y, x), index)

        for index, y, x in AbaloneModel.pos_generator(5):
            self.assertTrue(index < AbaloneModel.get_field_size(5))
            self.assertEqual(model5.get_1d_pos(y, x), index)

    def test_2d_2_1d_pos(self):
        # Model 3
        for n in model3_pos_list:
            self.assertEqual(model3.get_1d_pos(*n[0]), n[1])

        # Model 5
        for n in model5_pos_list:
            self.assertEqual(model5.get_1d_pos(*n[0]), n[1])

    def test_1d_2_2d_pos(self):
        # Model 3
        for n in model3_pos_list:
            self.assertEqual(model3.get_2d_pos(n[1]), n[0])

        # Model 5
        for n in model5_pos_list:
            self.assertEqual(model5.get_2d_pos(n[1]), n[0])

    def test_validation_pos(self):
        # Model 3
        for n in model3_validation_pos:
            self.assertEqual(model3.check_valid_pos(*n[0]), n[1])

        # Model 5
        for n in model5_validation_pos:
            self.assertEqual(model5.check_valid_pos(*n[0]), n[1])

    def test_to_vector(self):
        self.assertTrue(np.array_equal(model3.game_vector, np.array([0] * (model3.field_size + 5))))
        self.assertTrue(np.array_equal(model5.game_vector, np.array([0] * (model5.field_size + 5))))

    def field_size_2_edge_size(self):
        self.assertTrue(AbaloneModel.get_edge_size(model3.field_size), model3.edge_size)
        self.assertTrue(AbaloneModel.get_edge_size(model5.field_size), model5.edge_size)

    def test_can_push_stone(self):
        pass

    def test_push_stone(self):
        pass

    def test_end_game(self):
        pass
