from agent.reward.RewardModule import RewardModule


class SuccessMoveReward(RewardModule):

    def __init__(self, success_reward: int = 1):
        super().__init__()
        self.success_reward = success_reward

    def get_reward(self, success: bool, turns: int, out: int, end: bool, win: bool) -> float:
        rwd = 0
        if success:
            rwd = self.success_reward
        return rwd

    def dim(self, ratio: int = 0.5):
        self.success_reward = self.success_reward * ratio
