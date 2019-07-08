import numpy as np

from abalone.StoneColor import StoneColor


def get_text_board(game_vector: np.ndarray) -> str:
    rs_str = (chr(32) * (game_vector[0] + 3)) + "".join([str(i + 1) + " " for i in range(game_vector[0])])
    tef = (lambda w: "+" if w == StoneColor.NONE.value else ("@" if w == StoneColor.BLACK.value else "O"))
    for n in range(game_vector[0] * 2 - 1):
        if n < game_vector[0]:
            y = int(((n + game_vector[0] - 1) * (n + game_vector[0]) - (game_vector[0] - 1) * game_vector[0]) / 2)
            rs_str = "".join(chr(32) * (game_vector[0] - n)) + chr(65 + n) + " " \
                     + "".join([tef(game_vector[y + c]) + " " for c in range(game_vector[0] + n)]) \
                     + (lambda v: "" if v > game_vector[0] - 2 else str(game_vector[0] + v + 1))(n) + "\n" + rs_str
        else:
            y = int((n * (6 * game_vector[0] - n - 5) + -2 * game_vector[0] * (game_vector[0] - 2) - 2) / 2)
            rs_str = "".join(chr(32) * (n - game_vector[0] + 1)) + " " + chr(65 + n) + " " \
                     + "".join([tef(game_vector[y + c]) + " " for c in range(game_vector[0] * 3 - n - 2)]) \
                     + "\n" + rs_str
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
