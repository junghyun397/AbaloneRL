import unittest

from abalone import AbaloneModel, FieldTemplate
from agent.RandomPruningPolicy import RandomPruningPolicy
from model.AbaloneMCTS import AbaloneMCTS

model5 = AbaloneModel.AbaloneAgent(edge_size=5, vector_generator=FieldTemplate.basic_start)

pruning_policy = RandomPruningPolicy()
mcts = AbaloneMCTS(abalone_agent=model5, pruning_policy=pruning_policy)


class TestAbaloneMCTS(unittest.TestCase):

    def test_process_turn(self):
        mcts.process_game(model5.game_vector)

    def test_find_best_with_random_policy(self):
        mcts.process_game(model5.game_vector)

    def test_find_best_with_unlimited_depth(self):
        mcts.process_game(model5.game_vector)
