from abc import ABCMeta, abstractmethod


class TrainAgent(metaclass=ABCMeta):

    @abstractmethod
    def fit(self) -> None:
        pass
