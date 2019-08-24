import copy

import numpy as np

from abalone import AbaloneModel
from agent.PruningPolicy import PruningPolicy


def prob_array(x: np.ndarray) -> np.ndarray:
    return x / x.sum(axis=0)


class AbaloneMCTS:

    def __init__(self,
                 abalone_agent: AbaloneModel.AbaloneAgent,
                 pruning_policy: PruningPolicy,
                 max_depth: int = 100):
        self.agent = copy.deepcopy(abalone_agent)
        self.pruning_policy = pruning_policy
        self._max_depth = max_depth

        self.agent.set_game_vector(np.array([0]))

    def get_action_prob(self, game_vector: np.ndarray) -> np.ndarray:
        nodes = list()
        action_count = AbaloneModel.get_action_size(game_vector.size)
        for action in range(action_count):
            nodes.append(self.search(game_vector.copy()))
        return prob_array(nodes)

    def search(self, game_vector: np.ndarray):
        pass
