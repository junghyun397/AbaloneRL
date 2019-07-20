from abc import ABCMeta, abstractmethod

import numpy as np


class NeuralNetwork(metaclass=ABCMeta):

    @abstractmethod
    def forward(self, x: np.ndarray) -> np.ndarray:
        pass

    @abstractmethod
    def backward(self, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        pass
