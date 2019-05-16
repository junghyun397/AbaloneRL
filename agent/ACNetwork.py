from abc import ABCMeta, abstractmethod

import numpy as np


class ACNetwork(metaclass=ABCMeta):

    @abstractmethod
    def build_network(self):
        pass

    @abstractmethod
    def forward(self, x: np.ndarray) -> np.ndarray:
        pass

    @abstractmethod
    def backward(self, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        pass
