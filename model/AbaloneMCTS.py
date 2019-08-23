import numpy as np

from abalone import AbaloneModel
from agent.PruningPolicy import PruningPolicy


class Node:

    def __init__(self, parent):
        self._parent = parent
        self._child = dict()

    def expand(self):
        pass

    def select(self):
        pass

    def update(self):
        pass

    def update_all(self):
        pass

    def calculate(self):
        pass


class AbaloneMCTS:

    def __init__(self,
                 abalone_agent: AbaloneModel.AbaloneAgent,
                 pruning_policy: PruningPolicy,
                 max_depth: int = 100):
        self.agent = abalone_agent
        self.pruning_policy = pruning_policy

        self._max_depth = max_depth
        self._root = Node(None)

    def get_action_scores(self, game_vector: np.ndarray):
        pass

    def _next(self, game_vector: np.ndarray):
        pass
