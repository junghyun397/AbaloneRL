import numpy as np

from abalone.StoneColor import StoneColor


class AbaloneModel:
    EDGE_SIZE = 5

    def __init__(self,
                 edge_size: int = EDGE_SIZE,
                 field: np.ndarray = np.zeros((3 * pow(EDGE_SIZE, 2) - 3 * EDGE_SIZE + 1,)),
                 turns: int = 0,
                 out_black: int = 0,
                 out_white: int = 0,
                 cur_color: StoneColor = StoneColor.NONE, ):
        self.edge_size = edge_size
        self.field = field
        self.turns = turns
        self.out_black = out_black
        self.out_white = out_white
        self.cur_color = cur_color

    # Logic Filed Control

    def try_move_stone(self, stones: tuple, description: int, color: StoneColor) -> bool:
        if self.can_move_stone(stones, description, color):
            self.move_stone(stones, description, color)
            return True
        return False

    def can_move_stone(self, stones: tuple, description: int, color: StoneColor) -> bool:
        pass

    def move_stone(self, stones: tuple, description: int, color: StoneColor) -> None:
        pass

    # Bin Field Control

    def set_field_stone(self, index: int, color: StoneColor) -> None:
        self.field[index] = color

    def get_field_stone(self, index: int) -> int:
        return self.field[index]

    # Position Data

    def get_1d_pos(self, y: int, x: int) -> int:
        if y < self.edge_size:
            return int(
                ((y + self.edge_size - 1) * (y + self.edge_size)) / 2 - ((self.edge_size - 1) * self.edge_size) / 2 + x)
        else:
            return int(
                ((y + self.edge_size - 1) * (y + self.edge_size)) / 2 - ((self.edge_size - 1) * self.edge_size) / 2 - ((y - self.edge_size) * (y - self.edge_size + 1)) + x - (y - self.edge_size) - 1)

    # Bin Data

    def copy(self):
        return AbaloneModel(edge_size=self.edge_size, field=self.copy_field(), turns=self.turns, out_black=self.out_black, out_white=self.out_white, cur_color=self.cur_color)

    def copy_field(self) -> np.ndarray:
        return np.copy(self.field)

    # Utility

    def to_text(self) -> str:
        return ''.join([str(b) for b in range(self.edge_size * 2 - 1)])

    # Private

    def _next_turn(self) -> None:
        self.turns += 1
        self._flip_color()

    def _flip_color(self) -> None:
        if self.cur_color == StoneColor.BLACK:
            self.cur_color = StoneColor.WHITE
        else:
            self.cur_color = StoneColor.BLACK
