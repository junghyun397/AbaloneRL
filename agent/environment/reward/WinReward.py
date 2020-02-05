from agent.environment.reward.RewardModule import RewardModule


class WinReward(RewardModule):

    def __init__(self, win_reward: int = 100):
        super().__init__()
        self.win_reward = win_reward

    def get_reward(self, success: bool, turns: int, out: int, end: bool, win: bool) -> float:
        if win:
            return self.win_reward
        else:
            return 0

    def dim(self, ratio: float = 0.5):
        self.win_reward = self.win_reward * ratio
