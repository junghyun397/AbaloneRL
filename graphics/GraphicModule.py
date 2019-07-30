from abc import abstractmethod, ABCMeta

import numpy as np


class GraphicModule(metaclass=ABCMeta):

    def __init__(self, base_vector: np.ndarray) -> None:
        self.base_vector = base_vector

    @abstractmethod
    def draw(self) -> None:
        pass

    def set_vector(self, new_vector: np.ndarray) -> None:
        self.base_vector = new_vector
