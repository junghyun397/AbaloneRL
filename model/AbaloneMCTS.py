from typing import Optional, List, Tuple, Dict, Iterator

import numpy as np

from abalone import AbaloneModel
from agent.PruningPolicy import PruningPolicy


class AbaloneMCTS:

    def __init__(self,
                 abalone_agent: AbaloneModel.AbaloneAgent,
                 pruning_policy: PruningPolicy):
        super().__init__()
        self.agent = abalone_agent
        self.t_agent = abalone_agent.copy()
        self.pruning_policy = pruning_policy

    def process_episode(self, state_vector: np.ndarray) -> List[float]:
        t_tree = dict()
        n_tree = dict()
        return [0, 0, 0]

    def process_turn(self, state_vector: np.ndarray) -> None:
        for n_vector, moved in self.find_possible_move((state_vector, 0)):
            if moved > 2:
                self.find_possible_move((n_vector, moved))

    def find_possible_move(self, state: Tuple[np.ndarray, int]) -> Iterator[Tuple[np.ndarray, int]]:
        for act in range(self.agent.field_size):
            self.t_agent.set_game_vector(state[0].copy())
            success, moved, _ = self.t_agent.can_push_stone(*self.agent.decode_action(act))
            if success is not None and state[1] + moved <= 3:
                self.t_agent.set_game_vector(state[0].copy())
                self.t_agent.push_stone(*self.agent.decode_action(act))
                yield self.t_agent.game_vector, state[1] + moved
