from typing import Tuple

import numpy as np

from abalone import AbaloneModel, FieldTemplate
from abalone.HexDescription import HexDescription
from agent.Environment import Environment
from agent.reward.RewardModule import RewardModule
from agent.reward.SuccessMoveReward import SuccessMoveReward


class AbaloneEnvironment(Environment):

    def __init__(self,
                 abalone_model: AbaloneModel.AbaloneAgent = AbaloneModel.AbaloneAgent(edge_size=5,
                                                                                      use_indexed_pos=True,
                                                                                      vector=FieldTemplate.get_basic_start(5))):
        super().__init__(abalone_model.field_size * 6)
        self.abalone_model = abalone_model

    def action(self, action: list) -> (np.ndarray, Tuple[bool, bool, bool], Tuple[int, int, int], int, bool, bool):
        success = (False, False, False)
        drops = (0, 0, 0)
        end, win, cut_out = False, False, 0
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

        return self.abalone_model.game_vector, success, drops, cut_out, win, end

    def get_state(self) -> np.ndarray:
        return self.abalone_model.game_vector

    def decode_action(self, action: int) -> (int, int, HexDescription):
        y, x = self.abalone_model.get_2d_pos(action // 6)
        return y, x, HexDescription(action % 6 + 1)
