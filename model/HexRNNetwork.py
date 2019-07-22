import numpy as np

from agent.NeuralNetwork import NeuralNetwork


class HexRNNetwork(NeuralNetwork):

    def __init__(self):
        super().__init__()
        self._build_model()

    def _build_model(self):
        pass

    def forward(self, x: np.ndarray) -> np.ndarray:
        pass

    def backward(self, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        pass
