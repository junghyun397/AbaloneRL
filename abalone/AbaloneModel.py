import numpy as np

from abalone.StoneColor import StoneColor


class AbaloneModel:
    EDGE_SIZE = 5

    def __init__(self,
                 field: np.ndarray = np.zeros((3 * pow(EDGE_SIZE, 2) - 3 * EDGE_SIZE + 1,), dtype=np.int8),
                 turns: int = 0,
                 out_black: int = 0,
                 out_white: int = 0,
                 cur_color: StoneColor = StoneColor.NONE, ):
        self.field = field
        self.turns = turns
        self.out_black = out_black
        self.out_white = out_white
        self.cur_color = cur_color

        self.edge_size = AbaloneModel.EDGE_SIZE

    def next_turn(self):
        self.turns += 1
        self._flip_color()

    def set_field_stone(self, x: int, y: int, color: StoneColor):
        self.field[self.get_1d_pos(x, y)] = color

    def get_field_stone(self, x: int, y: int) -> int:
        return self.field[self.get_1d_pos(x, y)]

    def get_1d_pos(self, x: int, y: int) -> int:
        pass

    def copy(self):
        return AbaloneModel(field=self.copy_field(), turns=self.turns, out_black=self.out_black, out_white=self.out_white, cur_color=self.cur_color)

    def copy_field(self) -> np.ndarray:
        return np.copy(self.field)

    def _flip_color(self):
        if self.cur_color == StoneColor.BLACK:
            self.cur_color = StoneColor.WHITE
        else:
            self.cur_color = StoneColor.BLACK
