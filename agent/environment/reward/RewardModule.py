from abc import ABCMeta, abstractmethod


class RewardModule(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_reward(self, success: bool, turns: int, out: int, end: bool, win: bool) -> float:
        pass

    @abstractmethod
    def dim(self, ratio: int):
        pass
