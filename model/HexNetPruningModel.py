import numpy as np

from agent.PruningPolicy import PruningPolicy


class HexNetPruningModel(PruningPolicy):

    def prediction(self, source_vector: np.ndarray) -> float:
        pass
