from typing import Optional, List, Tuple, Dict

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
        pass

    def process_turn(self, state_vector: np.ndarray) -> None:
        merged = self.find_next_move((state_vector, 0))
        if merged is not None:
            for state, act in merged:
                self.process_turn(state)

    def find_next_move(self, state: Tuple[np.ndarray, int]) -> Optional[Dict[Tuple[np.ndarray, int]]]:
        self.t_agent.set_game_vector(state[0])
        merged_vec = dict()
        for act in range(self.agent.field_size):
            self.t_agent.set_game_vector(state[0].copy())
            success, moved, _ = self.t_agent.try_push_stone(*self.agent.decode_action(act))
            if success and state[1] + moved <= 3:
                merged_vec[act] = self.t_agent.game_vector, state[1] + moved
        return None if len(merged_vec) == 0 else merged_vec
