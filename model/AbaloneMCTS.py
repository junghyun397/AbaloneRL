import copy
from typing import Dict

import numpy as np

from abalone import AbaloneModel
from agent.PruningPolicy import PruningPolicy


def prob_array(x: np.ndarray) -> np.ndarray:
    return x / x.sum(axis=0)


class Node:

    def __init__(self, parent,
                 child: dict = None,
                 prv_prob: int = 0):
        self.parent = parent
        self.child = dict() if child is None else child
        self.prv_prob = prv_prob

        self.visit_count = 0

        self._q_value = 0
        self._u_value = 0

    def expand(self, action_prob: Dict[int, float]) -> None:
        for action, prob in action_prob:
            if action not in self.child:
                self.child[action] = Node(self, prv_prob=prob)

    def select(self, bound: float):
        max_score, max_node = 0, None
        for node in self.child.items():
            if node[1].get_score(bound) > max_score:
                max_score, max_node = node[1].get_score(bound), node
        return max_node

    def update(self, prn: float) -> None:
        self.visit_count += 1
        self._q_value = (prn - self._q_value) / self.visit_count

    def update_all(self, prn: float) -> None:
        if self.parent is not None:
            self.parent.update_recursive(-prn)
        self.update(prn)

    def get_score(self, cutoff: float) -> float:
        self._u_value = (cutoff * self.prv_prob * np.sqrt(self.parent.visit_count) / (1 + self.visit_count))
        return self._q_value + self._u_value


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

    def forward_move(self):
        pass
