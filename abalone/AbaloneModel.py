from typing import Optional

import numpy as np

from abalone.HexDescription import HexDescription
from abalone.StoneColor import StoneColor


def new_field(size: int) -> np.ndarray:
    return np.zeros((3 * pow(size, 2) - 3 * size + 1,), dtype=np.int8)


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
            field = new_field(edge_size)
        self.field = field

        self.turns = turns
        self.cur_color = cur_color

        self.out_black = out_black
        self.out_white = out_white

        self._cur_out_black = 0
        self._cur_out_white = 0

    # Game Control

    def next_turn(self) -> (int, int, Optional[StoneColor]):
        self.out_black += self._cur_out_black
        self.out_white += self._cur_out_white
        temp_out_black, temp_out_white = self._cur_out_black, self._cur_out_white

        self._cur_out_black, self._cur_out_white = 0, 0
        self.turns += 1
        self._flip_color()
        return temp_out_black, temp_out_white, self.is_win()

    # Logic Filed Control

    def try_push_stone(self, y: int, x: int, description: HexDescription) -> bool:
        line = self.can_push_stone(y, x, description)
        if line is None:
            return False
        self.push_stone(y, x, description, line)
        return True

    def can_push_stone(self, y: int, x: int, description: HexDescription) -> Optional[list]:
        line = self.get_line(y, x, description)
        if len(line) < 2:
            return None

        my_count, opp_count = 0, 0
        for s in line:
            if s == self.cur_color.value:
                my_count += 1
            elif s != 0:
                if opp_count > my_count:
                    return None
                opp_count += 1
            else:
                if my_count > opp_count:
                    return line

            if my_count > 3 or opp_count > 3:
                return None

    def push_stone(self, y: int, x: int, description: HexDescription, line: list = None) -> None:
        if line is None:
            line = self.get_line(y, x, description)

        if line[len(line) - 1] == StoneColor.BLACK.value:
            self.out_black += 1
        elif line[len(line) - 1] == StoneColor.WHITE.value:
            self.out_white += 1

        line = [0] + line.pop()
        self.set_line(y, x, description, line)

    # Game Observe

    def is_win(self) -> Optional[StoneColor]:
        if self.out_white > 5:
            return StoneColor.BLACK
        elif self.out_black > 5:
            return StoneColor.WHITE
        return None

    # Bin Field Control

    def get_line(self, y: int, x: int, description: HexDescription) -> list:
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

    def set_line(self, y: int, x: int, description: HexDescription, line: list) -> None:
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

    def set_field_stone(self, y: int, x: int, color: StoneColor) -> None:
        self.field[self.get_1d_pos(y, x)] = color.value

    def get_field_stone(self, y: int, x: int) -> int:
        return self.field[self.get_1d_pos(y, x)]

    # Position Data

    def get_1d_pos(self, y: int, x: int) -> int:
        if y < self.edge_size:
            return int(y * (-y + 2 * self.edge_size + 1) / 2) + x
        else:
            return int((y * (-y + 6 * self.edge_size - 5) + -2 * self.edge_size * (self.edge_size - 2) - 2) / 2) + x

    def get_2d_pos(self, index: int) -> (int, int):
        if index > self.field.size // 2:
            pass
        else:
            pass

    def check_valid_pos(self, y: int, x: int) -> bool:
        if y < self.edge_size:
            return y < self.edge_size * 2 and self.edge_size + y > x > -1
        else:
            return y < self.edge_size * 2 and y - self.edge_size < x < self.edge_size * 2 - 1

    # Bin Data

    def reset(self) -> None:
        self.field = new_field(self.edge_size)
        self.turns = 0
        self.cur_color = StoneColor.BLACK
        self.out_black, self.out_white = 0, 0

    def copy(self):
        return AbaloneModel(edge_size=self.edge_size, field=self.copy_field(),
                            turns=self.turns, cur_color=self.cur_color,
                            out_black=self.out_black, out_white=self.out_white)

    def copy_field(self) -> np.ndarray:
        return np.copy(self.field)

    def to_vector(self) -> np.ndarray:
        return np.append(self.copy_field(), np.array([self.out_black, self.out_white, self.turns], dtype=np.int8))

    # Private

    def _flip_color(self) -> None:
        if self.cur_color == StoneColor.BLACK:
            self.cur_color = StoneColor.WHITE
        else:
            self.cur_color = StoneColor.BLACK
