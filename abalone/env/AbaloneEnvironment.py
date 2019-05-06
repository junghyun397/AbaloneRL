import numpy as np

from abalone.AbaloneModel import AbaloneModel
from abalone.FieldTemplate import FieldTemplate
from abalone.HexDescription import HexDescription
from abalone.StoneColor import StoneColor
from agent.Environment import Environment
from agent.reward.RewardModule import RewardModule
from agent.reward.SuccessMoveReward import SuccessMoveReward


class AbaloneEnvironment(Environment):

    def __init__(self,
                 abalone_model: AbaloneModel = AbaloneModel(edge_size=5, field=FieldTemplate.EDGE_5_BELGIAN_DAISY),
                 reward_module: RewardModule = SuccessMoveReward()):
        self.abalone_model = abalone_model
        self.reward_module = reward_module

    def action(self, action: int) -> (np.ndarray, float, bool):
        y, x, description = self.decode_action(action)
        success = self.abalone_model.try_push_stone(y, x, description)
        out_black, out_white, winner = self.abalone_model.next_turn()
        field = self.abalone_model.copy_field()

        end, win = False, False
        if winner is not None:
            if winner != self.abalone_model.cur_color:
                win = True
            end = True
            self.abalone_model.reset()

        if self.abalone_model.cur_color == StoneColor.BLACK:
            out = out_black
        else:
            out = out_white

        return field, self.reward_module.get_reward(success, self.abalone_model.turns, out, end, win), end

    def get_state(self) -> np.ndarray:
        return self.abalone_model.copy_field()

    def decode_action(self, action: int) -> (int, int, HexDescription):
        l6 = action // 6
        y, x = self.abalone_model.get_2d_pos(l6)
        return y, x, HexDescription(action - (6 * l6))
