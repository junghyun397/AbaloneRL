import unittest

from abalone import AbaloneModel, FieldTemplate

model3 = AbaloneModel.AbaloneAgent(edge_size=3, vector_generator=FieldTemplate.empty_start)
model5 = AbaloneModel.AbaloneAgent(edge_size=5, vector_generator=FieldTemplate.empty_start)
model10 = AbaloneModel.AbaloneAgent(edge_size=10, vector_generator=FieldTemplate.empty_start)


class TestAbaloneLogic(unittest.TestCase):

    def test_select_stone(self):
        pass

    def test_push_stone(self):
        pass

    def test_next_turn(self):
        pass

    def test_end_game(self):
        pass
