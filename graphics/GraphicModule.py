from abc import abstractmethod, ABCMeta

import numpy as np


class GraphicModule(metaclass=ABCMeta):

    def __init__(self):
        self.base_vector = None

    @abstractmethod
    def draw(self) -> None:
        pass

    def set_vector(self, new_vector: np.ndarray) -> None:
        self.base_vector = new_vector
