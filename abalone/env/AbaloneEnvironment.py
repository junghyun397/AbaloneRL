from typing import Tuple, List

import numpy as np

from abalone import AbaloneModel, FieldTemplate
from abalone.HexDescription import HexDescription
from agent.Environment import Environment


class AbaloneEnvironment(Environment):

    def __init__(self,
                 abalone_agent: AbaloneModel.AbaloneAgent =
                 AbaloneModel.AbaloneAgent(edge_size=5,
                                           use_indexed_pos=True,
                                           vector=FieldTemplate.get_basic_start(5))):
        super().__init__(abalone_agent.field_size * 6)
        self.abalone_model = abalone_agent

    # Info Vector Index
    # success, drops, cut-put pos, is-win, is-end

    def action(self, action: List[int]) -> (np.ndarray, Tuple[List[bool], List[int], int, bool, bool]):
        success = [False, False, False]
        drops = [0, 0, 0]
        cut_out, end, win = 0, False, False
        for i in range(3):
            y, x, description = self.decode_action(action[i])
            success[i], do_end, drops[i] = self.abalone_model.try_push_stone(y, x, description)
            if do_end:
                cut_out = i
                break

        winner = self.abalone_model.next_turn()
        if winner is not None:
            if winner.value != self.abalone_model.game_vector[2]:
                win = True
            end = True
            self.abalone_model.reset(FieldTemplate.get_basic_start(self.abalone_model.edge_size))

        return self.abalone_model.game_vector, (success, drops, cut_out, win, end)

    def get_state(self) -> np.ndarray:
        return self.abalone_model.game_vector

    def decode_action(self, action: int) -> (int, int, HexDescription):
        y, x = self.abalone_model.get_2d_pos(action // 6)
        return y, x, HexDescription(action % 6 + 1)
