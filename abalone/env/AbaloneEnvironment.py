from typing import Tuple, List, Optional

import numpy as np

from abalone import AbaloneModel, FieldTemplate
from abalone.StoneColor import StoneColor
from agent.Environment import Environment


class AbaloneEnvironment(Environment):

    def __init__(self,
                 abalone_agent: AbaloneModel.AbaloneAgent =
                 AbaloneModel.AbaloneAgent(edge_size=5,
                                           use_indexed_pos=True,
                                           vector_generator=FieldTemplate.get_basic_start)):
        super().__init__(action_space=abalone_agent.field_size * 6)
        self.abalone_model = abalone_agent

    # Info Vector Index
    # success, drops, cut-put pos, is-win, is-end

    def action(self, action: List[int]) -> (List[Optional[np.ndarray]], Tuple[List[bool], List[int], int, bool, bool]):
        stats = [None] * self.abalone_model.role_vector[1]
        success = [False] * self.abalone_model.role_vector[1]
        drops = [0] * self.abalone_model.role_vector[1]
        cut_out, end, win, c_move_stone = 0, False, False, 0
        for i in range(self.abalone_model.role_vector[1]):
            y, x, description = self.abalone_model.decode_action(action[i])
            success[i], move_stone, drops[i] = self.abalone_model.try_push_stone(y, x, description)
            c_move_stone += move_stone
            stats[i] = self.abalone_model.game_vector.copy()
            if c_move_stone >= self.abalone_model.role_vector[1]:
                cut_out = i
                break

        winner = self.abalone_model.next_turn()
        if winner is not None:
            if winner.value != self.abalone_model.game_vector[2] and winner != StoneColor.NONE:
                win = True
            end = True
            self.abalone_model.reset()

        return stats, (success, drops, cut_out, win, end)

    def get_state(self) -> np.ndarray:
        return self.abalone_model.game_vector
