from agent.reward.RewardModule import RewardModule


class WinReward(RewardModule):

    def __init__(self):
        super().__init__()

    def get_reward(self, success: bool, turns: int, out: int, end: bool, win: bool) -> float:
        if win:
            return 100
        else:
            return 0
