import numpy as np


stone_blank = "*"
stone_black = "B"
stone_white = "W"

fixed_width_char = []


def get_text_board(abalone_vector: np.ndarray) -> str:
    pass


def load_text_board(text_board: str) -> np.ndarray:
    pass


def load_bin_board(bin_board: bytearray) -> np.ndarray:
    pass


class Edge3:
    EDGE_3_EMPTY = np.array([0], dtype=np.int8)
    EDGE_3_BASE_START = np.array([0], dtype=np.int8)


class Edge5:
    EDGE_5_EMPTY = np.array([0], dtype=np.int8)
    EDGE_5_BASE_START = np.array([0], dtype=np.int8)
    EDGE_5_BELGIAN_DAISY = np.array([0], dtype=np.int8)
