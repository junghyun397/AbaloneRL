from abc import ABCMeta, abstractmethod

import numpy as np


class PruningPolicy(metaclass=ABCMeta):

    @abstractmethod
    def prediction(self, source_vector: np.ndarray) -> float:
        pass
