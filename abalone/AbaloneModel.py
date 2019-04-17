import numpy as np

from abalone.HexDescription import HexDescription
from abalone.StoneColor import StoneColor


class AbaloneModel:

    def __init__(self,
                 edge_size: int = 5,
                 field: np.ndarray = None,
                 out_black: int = 0,
                 out_white: int = 0,
                 turns: int = 0,
                 cur_color: StoneColor = StoneColor.BLACK):
        self.edge_size = edge_size
        if field is None:
            field = np.zeros((3 * pow(edge_size, 2) - 3 * edge_size + 1,))
        self.field = field

        self.out_black = out_black
        self.out_white = out_white

        self.turns = turns
        self.cur_color = cur_color

    # Logic Filed Control

    def try_pull_stone(self, stones: tuple, description: HexDescription, color: StoneColor) -> bool:
        if self.can_pull_stone(stones, description, color):
            self.pull_stone(stones, description, color)
            return True
        return False

    def can_pull_stone(self, stones: tuple, description: HexDescription, color: StoneColor) -> bool:
        pass

    def pull_stone(self, stones: tuple, description: HexDescription, color: StoneColor) -> None:
        pass

    def get_line(self, x: int, y: int, description: HexDescription) -> []:
        if description == HexDescription.XP:
            if y < self.edge_size:
                return [self.field[self.get_1d_pos(y, xp)] for xp in range(x, self.edge_size + y - 1)]
            else:
                return [self.field[self.get_1d_pos(y, xp)] for xp in range(x, self.edge_size * 2 - 2)]
        elif description == HexDescription.XM:
            if y < self.edge_size:
                return [self.field[self.get_1d_pos(y, xp)] for xp in range(0, x, -1)]
            else:
                return [self.field[self.get_1d_pos(y, xp)] for xp in range(y - self.edge_size + 1, x, -1)]
        elif description == HexDescription.YP:
            if x < self.edge_size:
                return [self.field[self.get_1d_pos(yp, x)] for yp in range(y, self.edge_size + x)]
            else:
                return [self.field[self.get_1d_pos(yp, x)] for yp in range(y, self.edge_size * 2 - 2)]
        elif description == HexDescription.YM:
            if x < self.edge_size:
                return [self.field[self.get_1d_pos(yp, x)] for yp in range(0, y, -1)]
            else:
                return [self.field[self.get_1d_pos(yp, x)] for yp in range(x - self.edge_size + 1, x, -1)]
        elif description == HexDescription.ZP:
            return [self.field[self.get_1d_pos(yp, xp)] for yp, xp in zip(range(y, self.edge_size * 2 - 2), range(x, self.edge_size * 2 - 2))]
        elif description == HexDescription.ZM:
            return [self.field[self.get_1d_pos(yp, xp)] for yp, xp in zip(range(0, y, -1), range(0, x, -1))]

    # Bin Field Control

    def set_field_stone(self, index: int, color: StoneColor) -> None:
        self.field[index] = color

    def get_field_stone(self, index: int) -> int:
        return self.field[index]

    # Position Data

    def get_1d_pos(self, y: int, x: int) -> int:
        if y < self.edge_size:
            return int(-y * (y - 2 * self.edge_size - 1) / 2) + x
        else:
            return int((y * (-y + 6 * self.edge_size - 5) + 2 * self.edge_size * (-self.edge_size + 2) - 2) / 2) + x

    def check_pos(self, y: int, x: int) -> bool:
        if y < self.edge_size:
            return not (y > self.edge_size * 2 - 2 or x > self.edge_size + y - 1)
        else:
            return not(y > self.edge_size * 2 - 2 or not x < y - self.edge_size)

    # Bin Data

    def copy(self):
        return AbaloneModel(edge_size=self.edge_size, field=self.copy_field(),
                            out_black=self.out_black, out_white=self.out_white, turns=self.turns, cur_color=self.cur_color)

    def copy_field(self) -> np.ndarray:
        return np.copy(self.field)

    # Private

    def _next_turn(self) -> None:
        self.turns += 1
        self._flip_color()

    def _flip_color(self) -> None:
        if self.cur_color == StoneColor.BLACK:
            self.cur_color = StoneColor.WHITE
        else:
            self.cur_color = StoneColor.BLACK
