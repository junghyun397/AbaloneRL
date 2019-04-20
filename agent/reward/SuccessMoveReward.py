from agent.reward.RewardModule import RewardModule


class SuccessMoveReward(RewardModule):

    def __init__(self):
        super().__init__()

    def get_reward(self, success: bool, turns: int, out: int, end: bool, win: bool) -> float:
        rwd = 0
        if success:
            rwd = 1
        return rwd
