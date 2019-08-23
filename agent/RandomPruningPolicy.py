import random

import numpy as np

from agent.PruningPolicy import PruningPolicy


class RandomPruningPolicy(PruningPolicy):

    def prediction(self, source_vector: np.ndarray) -> float:
        return random.random()
