import numpy as np

from abalone.AbaloneModel import AbaloneModel


class FieldTemplate:
    EDGE_5_BASE_START = np.array([0], dtype=np.int8)
    EDGE_5_BELGIAN_DAISY = np.array([0], dtype=np.int8)

    @staticmethod
    def get_text_board(abalone_model: AbaloneModel) -> str:
        pass

    @staticmethod
    def load_text_board(text_board: str) -> AbaloneModel:
        pass

    @staticmethod
    def load_bin_board(bin_board: int) -> AbaloneModel:
        pass
