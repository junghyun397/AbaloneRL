import numpy as np

from agent.pruning.PruningPolicy import PruningPolicy
from model.HexProbNetwork import HexProbNetwork


class HexNetPruningModel(PruningPolicy):

    def __init__(self, hex_prob_network: HexProbNetwork):
        self.hex_prob_network = hex_prob_network

    def prediction(self, source_vector: np.ndarray) -> float:
        return self.hex_prob_network.forward(x=source_vector)[0]
