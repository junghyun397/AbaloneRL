import numpy as np

from abalone.AbaloneModel import AbaloneModel
from abalone.StoneColor import StoneColor


stone_blank = "*"
stone_black = "B"
stone_white = "W"

fixed_width_char = []


class FieldTemplate:

    class Edge5:
        EDGE_5_BASE_START = np.array([0], dtype=np.int8)
        EDGE_5_BELGIAN_DAISY = np.array([0], dtype=np.int8)

    @staticmethod
    def get_text_board(abalone_model: AbaloneModel) -> str:
        rs_str = ""
        w_range = abalone_model.edge_size * 2 - 1

        def to_text(x: [int]) -> str:
            el_text = ""
            for n in x:
                if n == StoneColor.BLACK.value:
                    el_text.join(stone_black)
                elif n == StoneColor.WHITE.value:
                    el_text.join(stone_white)
                else:
                    el_text.join(stone_blank)
            return el_text

        m_shift_size, index_num, bound = abalone_model.edge_size, w_range, 0
        for y in range(w_range):
            index_num -= 1
            if y > abalone_model.edge_size:
                m_shift_size -= 1
            else:
                m_shift_size += 1
            rs_str.join(w_range - y)\
                .join(to_text([abalone_model.field[n] for n in range(m_shift_size * 2)]))\
                .join([abalone_model.field[0]]).join(str(index_num))
            bound += 1
        return rs_str

    @staticmethod
    def load_text_board(text_board: str) -> AbaloneModel:
        array_board = zip(text_board)
        size = 0
        w_range = size * 2 - 1
        rs_field = np.zeros((3 * size ** 2 - 3 * size + 1,), dtype=np.int8)

        m_shift_size = 0
        for y in range(w_range):
            pass
        return AbaloneModel()

    @staticmethod
    def load_bin_board(bin_board: bytearray) -> AbaloneModel:
        return AbaloneModel()
