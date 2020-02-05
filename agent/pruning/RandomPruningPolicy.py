import random
from typing import Dict

import numpy as np

from agent.pruning.PruningPolicy import PruningPolicy


class RandomPruningPolicy(PruningPolicy):

    def prediction(self, source_vector: np.ndarray) -> (Dict[int, float], float):
        return random.random()
