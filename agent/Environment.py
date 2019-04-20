from abc import ABCMeta, abstractmethod

import numpy as np


class Environment(metaclass=ABCMeta):

    @abstractmethod
    def action(self, action: int) -> (np.ndarray, bool):
        pass

    @abstractmethod
    def get_state(self) -> np.ndarray:
        pass
