import numpy as np

from agent.NeuralNetwork import NeuralNetwork


class HexRNNNetwork(NeuralNetwork):

    def __init__(self):
        self._build_model()

    def _build_model(self):
        pass

    def forward(self, x: np.ndarray) -> np.ndarray:
        pass

    def backward(self, x: np.ndarray, y: np.ndarray):
        pass
