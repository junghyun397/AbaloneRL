import itertools
from functools import partial
from operator import is_not

import numpy as np

from abalone import AbaloneModel
from abalone.StoneColor import StoneColor


def get_text_board(game_vector: np.ndarray) -> str:
    rs_str = (chr(32) * (game_vector[0] + 2)) + "".join([str(i + 1) + " " for i in range(game_vector[0])])
    tef, idx = (lambda w: "+" if w == StoneColor.NONE.value else ("@" if w == StoneColor.BLACK.value else "#")), 0
    ids = (lambda v: game_vector[0] + n if n < game_vector[0] else game_vector[0] * 3 - v - 2)
    for n in range(game_vector[0] * 2 - 1):
        if n < game_vector[0]:
            rs_str = "".join(chr(32) * (game_vector[0] - n - 1)) + chr(65 + n) + " " \
                     + " ".join([tef(game_vector[5 + idx + c]) for c in range(game_vector[0] + n)]) \
                     + (lambda v: "" if v > game_vector[0] - 2 else " " + str(game_vector[0] + v + 1))(n) \
                     + "\n" + rs_str
        else:
            rs_str = "".join(chr(32) * (n - game_vector[0])) + " " + chr(65 + n) + " " \
                     + " ".join([tef(game_vector[5 + idx + c]) for c in range(game_vector[0] * 3 - n - 2)]) \
                     + "\n" + rs_str
        idx += ids(n)
    return rs_str


def load_text_board(info_vector: list, text_board: str) -> np.ndarray:
    return np.array(info_vector +
                    list(filter(partial(is_not, None),
                                [(lambda v: 0 if v == "+" else
                                 (StoneColor.BLACK.value if v == "@" else
                                  (StoneColor.WHITE.value if v == "#" else None)))(i)
                                 for i in itertools.chain(*text_board.split("\n")[::-1])])))


def get_basic_start(edge_size: int) -> np.ndarray:
    game_vector = AbaloneModel.new_vector(edge_size)
    if edge_size < 5:
        game_vector.put([5] + np.arange(edge_size), StoneColor.BLACK.value)
        game_vector.put([game_vector.size - edge_size] + np.arange(edge_size), StoneColor.WHITE.value)
        if edge_size > 2:
            game_vector.put(([game_vector.size - edge_size - 2] - np.arange(edge_size - 1)), StoneColor.WHITE.value)
            game_vector.put([6 + edge_size] + np.arange(edge_size - 1), StoneColor.BLACK.value)
        return game_vector
    game_vector.put([5] + np.arange(edge_size * 2 + 1), StoneColor.BLACK.value)
    game_vector.put([edge_size * 2 + 8] + np.arange(edge_size - 2), StoneColor.BLACK.value)
    game_vector.put([game_vector.size - 1] - np.arange(edge_size * 2 + 1), StoneColor.WHITE.value)
    game_vector.put([game_vector.size - edge_size * 2 - 4] - np.arange(edge_size - 2), StoneColor.WHITE.value)
    return game_vector
