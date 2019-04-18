from typing import Optional

import numpy as np

from abalone.HexDescription import HexDescription
from abalone.StoneColor import StoneColor


class AbaloneModel:

    def __init__(self,
                 edge_size: int = 5,
                 field: np.ndarray = None,
                 turns: int = 0,
                 cur_color: StoneColor = StoneColor.BLACK,
                 out_black: int = 0,
                 out_white: int = 0):
        self.edge_size = edge_size
        if field is None:
            field = np.zeros((3 * pow(edge_size, 2) - 3 * edge_size + 1,))
        self.field = field

        self.turns = turns
        self.cur_color = cur_color

        self.out_black = out_black
        self.out_white = out_white

    # Logic Filed Control

    def try_pull_stone(self, x: int, y: int, description: HexDescription) -> bool:
        line = self.can_pull_stone(x, y, description)
        if line is not None:
            self.pull_stone(x, y, description, line)
            return True
        return False

    def can_pull_stone(self, x: int, y: int, description: HexDescription) -> Optional[list]:
        line = self.get_line(x, y, description)
        my_count, opp_count = 0, 0
        for s in line:
            if s == self.cur_color:
                if opp_count > 0:
                    return None
                my_count += 1
            elif s != StoneColor.NONE:
                opp_count += 1
                if not opp_count < my_count:
                    return None

            if my_count > 3 or opp_count > 2:
                return None
        return line

    def pull_stone(self, x: int, y: int, description: HexDescription, line: list = None) -> None:
        if line is None:
            line = self.get_line(x, y, description)

        if line[len(line) - 1] == StoneColor.BLACK:
            self.out_black += 1
        elif line[len(line) - 1] == StoneColor.WHITE:
            self.out_white += 1

        line = [0] + line
        line.pop()
        self.set_line(x, y, description, line)

    def get_line(self, x: int, y: int, description: HexDescription) -> list:
        if description == HexDescription.XP:
            if y < self.edge_size:
                return [self.field[self.get_1d_pos(y, xp)] for xp in range(x, self.edge_size + y - 1)]
            else:
                return [self.field[self.get_1d_pos(y, xp)] for xp in range(x, self.edge_size * 2 - 2)]
        elif description == HexDescription.XM:
            if y < self.edge_size:
                return [self.field[self.get_1d_pos(y, xp)] for xp in reversed(range(0, x))]
            else:
                return [self.field[self.get_1d_pos(y, xp)] for xp in reversed(range(y - self.edge_size + 1, x))]
        elif description == HexDescription.YP:
            if x < self.edge_size:
                return [self.field[self.get_1d_pos(yp, x)] for yp in range(y, self.edge_size + x)]
            else:
                return [self.field[self.get_1d_pos(yp, x)] for yp in range(y, self.edge_size * 2 - 2)]
        elif description == HexDescription.YM:
            if x < self.edge_size:
                return [self.field[self.get_1d_pos(yp, x)] for yp in reversed(range(0, y))]
            else:
                return [self.field[self.get_1d_pos(yp, x)] for yp in reversed(range(x - self.edge_size + 1, x))]
        elif description == HexDescription.ZP:
            return [self.field[self.get_1d_pos(yp, xp)] for yp, xp in zip(range(y, self.edge_size * 2 - 2), range(x, self.edge_size * 2 - 2))]
        elif description == HexDescription.ZM:
            return [self.field[self.get_1d_pos(yp, xp)] for yp, xp in zip(reversed(range(0, y)), reversed(range(0, x)))]

    def set_line(self, x: int, y: int, description: HexDescription, line: list) -> None:
        if description == HexDescription.XP:
            for index in range(len(line)):
                self.field[self.get_1d_pos(y, x + index)] = line[index]
        elif description == HexDescription.XM:
            for index in range(len(line)):
                self.field[self.get_1d_pos(y, x - index)] = line[index]
        elif description == HexDescription.YP:
            for index in range(len(line)):
                self.field[self.get_1d_pos(y + index, x)] = line[index]
        elif description == HexDescription.YM:
            for index in range(len(line)):
                self.field[self.get_1d_pos(y - index, x)] = line[index]
        elif description == HexDescription.ZP:
            for index in range(len(line)):
                self.field[self.get_1d_pos(y + index, x + index)] = line[index]
        elif description == HexDescription.ZM:
            for index in range(len(line)):
                self.field[self.get_1d_pos(y - index, x - index)] = line[index]

    # Bin Field Control

    def set_field_stone(self, index: int, color: StoneColor) -> None:
        self.field[index] = color

    def get_field_stone(self, index: int) -> int:
        return self.field[index]

    # Position Data

    def get_1d_pos(self, y: int, x: int) -> int:
        if y < self.edge_size:
            return int(y * (-y + 2 * self.edge_size + 1) / 2) + x
        else:
            return int((y * (-y + 6 * self.edge_size - 5) + -2 * self.edge_size * (self.edge_size - 2) - 2) / 2) + x

    def check_valid_pos(self, y: int, x: int) -> bool:
        if y < self.edge_size:
            return y < self.edge_size * 2 and self.edge_size + y > x > -1
        else:
            return y < self.edge_size * 2 and y - self.edge_size < x < self.edge_size * 2 - 1

    # Bin Data

    def copy(self):
        return AbaloneModel(edge_size=self.edge_size, field=self.copy_field(),
                            turns=self.turns, cur_color=self.cur_color,
                            out_black=self.out_black, out_white=self.out_white,)

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