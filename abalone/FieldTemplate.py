import itertools
import random
from functools import partial
from operator import is_not
from typing import List

import numpy as np

from abalone import AbaloneModel
from abalone.StoneColor import StoneColor


PIXEL_BLACK = "@"
PIXEL_WHITE = "#"
PIXEL_NONE = "+"


# Text-IO manager


def get_text_board(game_vector: np.ndarray) -> str:
    rs_str = (chr(32) * (game_vector[0] + 2)) + str().join([str(i + 1) + chr(32) for i in range(game_vector[0])])
    tef, idx = (lambda w: PIXEL_NONE if w == StoneColor.NONE.value else
        (PIXEL_BLACK if w == StoneColor.BLACK.value else PIXEL_WHITE)), 0
    for n in range(game_vector[0] * 2 - 1):
        if n < game_vector[0]:
            rs_str = str().join(chr(32) * (game_vector[0] - n - 1)) + chr(65 + n) + chr(32) \
                     + chr(32).join([tef(game_vector[5 + idx + c]) for c in range(game_vector[0] + n)]) \
                     + ("" if n > game_vector[0] - 2 else chr(32) + str(game_vector[0] + n + 1)) \
                     + "\n" + rs_str
        else:
            rs_str = str().join(chr(32) * (n - game_vector[0])) + chr(32) + chr(65 + n) + chr(32) \
                     + chr(32).join([tef(game_vector[5 + idx + c]) for c in range(game_vector[0] * 3 - n - 2)]) \
                     + "\n" + rs_str
        idx += game_vector[0] + n if n < game_vector[0] else game_vector[0] * 3 - n - 2
    return rs_str


def load_text_board(info_vector: List[int], text_board: str) -> np.ndarray:
    return np.array(info_vector +
                    list(filter(partial(is_not, None),
                        [StoneColor.NONE.value if i == PIXEL_NONE else
                        (StoneColor.BLACK.value if i == PIXEL_BLACK else
                        (StoneColor.WHITE.value if i == PIXEL_WHITE else None))
                        for i in itertools.chain(*text_board.split("\n")[::-1])])), dtype=AbaloneModel.FIELD_DTYPE)


# Game-Vector generator


def empty_start(edge_size: int) -> np.ndarray:
    return AbaloneModel.new_vector(edge_size)


def basic_start(edge_size: int) -> np.ndarray:
    game_vector = AbaloneModel.new_vector(edge_size)
    if edge_size < 5:
        game_vector.put([5] + np.arange(edge_size), StoneColor.WHITE.value)
        game_vector.put([game_vector.size - edge_size] + np.arange(edge_size), StoneColor.BLACK.value)
        if edge_size > 2:
            game_vector.put([6 + edge_size] + np.arange(edge_size - 1), StoneColor.WHITE.value)
            game_vector.put(([game_vector.size - edge_size - 2] - np.arange(edge_size - 1)), StoneColor.BLACK.value)
        return game_vector
    game_vector.put([5] + np.arange(edge_size * 2 + 1), StoneColor.WHITE.value)
    game_vector.put([edge_size * 2 + 8] + np.arange(edge_size - 2), StoneColor.WHITE.value)
    game_vector.put([game_vector.size - 1] - np.arange(edge_size * 2 + 1), StoneColor.BLACK.value)
    game_vector.put([game_vector.size - edge_size * 2 - 4] - np.arange(edge_size - 2), StoneColor.BLACK.value)
    return game_vector


def random_filled_start(edge_size: int, fill_ratio: float = .4) -> np.ndarray:
    game_vector = AbaloneModel.new_vector(edge_size)
    fill_ratio /= 2

    for current_color in (StoneColor.BLACK.value, StoneColor.WHITE.value):
        for f_idx in range(int((game_vector.size - 5) * fill_ratio // 1)):
            while True:
                pos = 5 + int(random.random() * (game_vector.size - 5) // 1)
                if game_vector[pos] == StoneColor.NONE.value:
                    game_vector[pos] = current_color
                    break
    return game_vector
