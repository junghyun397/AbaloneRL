import math
from typing import Callable, Tuple

import numpy as np


def get_field_size(edge_size: int) -> int:
    return 3 * edge_size ** 2 - 3 * edge_size + 1


def get_edge_size(field_size: int) -> int:
    return int((3 + math.sqrt(12 * field_size - 3)) / 6)


def get_pos_method(edge_size: int) -> (Callable[[int, int], int], Callable[[int], Tuple[int, int]]):
    def get_1d_pos(y: int, x: int) -> int:
        if y < edge_size:
            return int(y * (-y + 2 * edge_size + 1) / 2) + x
        else:
            return int((y * (-y + 6 * edge_size - 5) + -2 * edge_size * (edge_size - 2) - 2) / 2) + x

    def get_2d_pos(index: int) -> (int, int):
        if index < edge_size:
            return 0, 0
        else:
            return 0, 0

    return get_1d_pos, get_2d_pos


def new_field(size: int) -> np.ndarray:
    return np.zeros((get_field_size(size),), dtype=np.int8)


def new_vector(size: int) -> np.ndarray:
    return np.zeros((5 + get_field_size(size),), dtype=np.int8)
