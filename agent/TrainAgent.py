from abc import ABCMeta, abstractmethod


class TrainAgent(metaclass=ABCMeta):

    @abstractmethod
    def train(self) -> None:
        pass
