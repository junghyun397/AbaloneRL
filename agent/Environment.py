from abc import ABCMeta, abstractmethod
from typing import List, Tuple

import numpy as np


class Environment(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, action_space: int):
        self.action_space = action_space

    @abstractmethod
    def action(self, action: List[int]) -> (List[np.ndarray], Tuple[List[bool], List[int], int, bool, bool]):
        pass

    @abstractmethod
    def get_state(self) -> np.ndarray:
        pass
