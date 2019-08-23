import unittest

from abalone import AbaloneModel, FieldTemplate
from agent.RandomPruningPolicy import RandomPruningPolicy
from model.AbaloneMCTS import AbaloneMCTS

model5 = AbaloneModel.AbaloneAgent(edge_size=5, vector_generator=FieldTemplate.basic_start)

pruning_policy = RandomPruningPolicy()
mcts = AbaloneMCTS(abalone_agent=model5, pruning_policy=pruning_policy)


class TestAbalone(unittest.TestCase):

    def test_process_turn(self):
        pass

    def test_find_with_random_policy(self):
        pass

    def test_find_with_unlimited_depth(self):
        pass
