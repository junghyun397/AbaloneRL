import numpy as np

from abalone import AbaloneModel
from abalone.StoneColor import StoneColor

stone_blank = "+"
stone_black = "@"
stone_white = "O"


def _get_text_shape(code: int) -> str:
    if code == StoneColor.BLACK.value:
        return "@"
    elif code == StoneColor.WHITE.value:
        return "O"
    else:
        return "+"


def get_text_board(game_vector: np.ndarray) -> str:
    rs_str = (chr(32) * (game_vector[0] + 3)) + "".join([str(i + 1) + " " for i in range(game_vector[0])])
    for n in range(game_vector[0] * 2 - 1):
        if n < game_vector[0]:
            y = int(((n + game_vector[0] - 1) * (n + game_vector[0]) - (game_vector[0] - 1) * game_vector[0]) / 2)
            rs_str = "".join(chr(32) * (game_vector[0] - n)) + str(n + 1) + " " \
                     + "".join([_get_text_shape(game_vector[y + c]) + " " for c in range(game_vector[0] - n)]) + str(game_vector[0] + n + 1) + "\n" + rs_str
        else:
            y = int((n * (6 * game_vector[0] - n - 5) + -2 * game_vector[0] * (game_vector[0] - 2) - 2) / 2)
            rs_str = "".join(chr(32) * (n - game_vector[0] + 2)) + " " + str(n + 1) + " " \
                     + "".join([_get_text_shape(game_vector[y + c]) + " " for c in range(game_vector[0] + n)]) + "\n" + rs_str
    return rs_str


def load_text_board(text_board: str) -> np.ndarray:
    text_board.replace("@", "1").replace("O", "2").replace("+", "0")
    return np.array(text_board, dtype=np.int8)


def load_bin_board(bin_board: bytearray) -> np.ndarray:
    pass


class Edge3:
    EDGE_3_EMPTY = np.array([0], dtype=np.int8)
    EDGE_3_BASE_START = np.array([0], dtype=np.int8)


class Edge5:
    EDGE_5_EMPTY = np.array([0], dtype=np.int8)
    EDGE_5_BASE_START = np.array([0], dtype=np.int8)
    EDGE_5_BELGIAN_DAISY = np.array([0], dtype=np.int8)
