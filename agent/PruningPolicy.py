from abc import ABCMeta, abstractmethod
from typing import Dict

import numpy as np


class PruningPolicy(metaclass=ABCMeta):

    @abstractmethod
    def prediction(self, source_vector: np.ndarray) -> (Dict[int, float], float):
        pass
