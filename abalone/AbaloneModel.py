import math
from itertools import zip_longest
from typing import Callable, Tuple, Optional, Iterator

import numpy as np

from abalone.HexDescription import HexDescription
from abalone.StoneColor import StoneColor


# Vector Size Control

def get_field_size(edge_size: int) -> int:
    return 3 * edge_size ** 2 - 3 * edge_size + 1


def get_edge_size(field_size: int) -> int:
    return int((3 + math.sqrt(12 * field_size - 3)) / 6)


# Indexed-Pos Generator

def pos_generator(edge_size: int) -> Iterator[Tuple[int, int, int]]:
    index, y, x = 0, 0, 0
    edge_cut, shift_x = edge_size, 0
    ef = (lambda v: -1 if v > edge_size - 2 else 1)
    while index < get_field_size(edge_size):
        if edge_cut == x:
            if y > edge_size - 2:
                shift_x += 1
            edge_cut += ef(y)
            y += 1
            x = 0
        yield index, y, x + shift_x
        index += 1
        x += 1


_indexed_pos = dict()


def _create_indexed_pos(edge_size: int) -> None:
    _indexed_pos[edge_size] = dict()
    for index, y, x in pos_generator(edge_size):
        _indexed_pos[edge_size][index] = y, x
        _indexed_pos[edge_size][y, x] = index


# Pos Generator

def get_pos_method(edge_size: int) -> (Callable[[int, int], int], Callable[[int], Tuple[int, int]]):
    def get_1d_pos(y: int, x: int) -> int:
        if y < edge_size:
            return int(((y + edge_size - 1) * (y + edge_size) - (edge_size - 1) * edge_size) / 2 + x)
        else:
            return int((y * (6 * edge_size - y - 5) + -2 * edge_size * (edge_size - 2) - 2) / 2 + x)

    def get_2d_pos(index: int) -> (int, int):
        if index < edge_size * (3 * edge_size - 1) / 2:
            return 0, 0
        else:
            return 0, 0

    return get_1d_pos, get_2d_pos


def get_indexed_pos_method(edge_size: int) -> (Callable[[int, int], int], Callable[[int], Tuple[int, int]]):
    if _indexed_pos.get(edge_size) is None:
        _create_indexed_pos(edge_size)

    temp_map = _indexed_pos[edge_size]

    def get_1d_pos(y: int, x: int) -> int:
        return temp_map[y, x]

    def get_2d_pos(index: int) -> (int, int):
        return temp_map[index]

    return get_1d_pos, get_2d_pos


# Field Generator

def new_field(edge_size: int) -> np.ndarray:
    return np.zeros((get_field_size(edge_size),), dtype=np.int8)


def new_vector(edge_size: int) -> np.ndarray:
    return np.array([edge_size] + [0] * (get_field_size(edge_size) + 4), dtype=np.int8)


# Game Vector Index
# 0 edge_size :: 1 turns :: 2 current color :: 3 out_black :: 4 out_white :: 5~ filed ~

class AbaloneAgent:

    def __init__(self,
                 edge_size: int = 5,
                 vector: np.ndarray = None,
                 use_indexed_pos: bool = False):
        if vector is None:
            vector = new_vector(edge_size)

        self.edge_size = edge_size
        self.game_vector = vector

        self.field_size = get_field_size(edge_size)

        if use_indexed_pos:
            self.get_1d_pos, self.get_2d_pos = get_indexed_pos_method(edge_size)
        else:
            self.get_1d_pos, self.get_2d_pos = get_pos_method(edge_size)

        self.current_move_stone = 0
        self.current_out_black = 0
        self.current_out_white = 0

    # Bin Data

    def set_game_vector(self, vector: np.ndarray) -> None:
        self.current_move_stone, self.current_out_black, self.current_out_white = 0, 0, 0
        self.game_vector = vector

    def reset(self, vector: np.ndarray = None):
        if vector is None:
            vector = new_vector(self.edge_size)
        self.game_vector = vector

    def copy(self):
        return AbaloneAgent(self.edge_size, np.copy(self.game_vector))

    def copy_vector(self) -> np.ndarray:
        return np.copy(self.game_vector)

    # Game Data

    def get_info(self) -> np.ndarray:
        return self.game_vector[::5]

    def get_filed(self) -> np.ndarray:
        return self.game_vector[5::]

    def get_turns(self) -> int:
        return self.game_vector[1]

    def get_current_color(self) -> int:
        return self.game_vector[2]

    def get_out_black(self) -> int:
        return self.game_vector[3]

    def get_out_white(self) -> int:
        return self.game_vector[4]

    # Game Control

    def next_turn(self) -> Optional[StoneColor]:
        self.current_move_stone = 0
        self.game_vector[1] += 1
        self._flip_color()
        if self.game_vector[4] > 5:
            return StoneColor.BLACK
        elif self.game_vector[3] > 5:
            return StoneColor.WHITE
        return None

    # Logic Filed Control

    def try_push_stone(self, y: int, x: int, description: HexDescription) -> (bool, bool, int):
        line, move_stone, dropped = self.can_push_stone(y, x, description)
        if line is None or move_stone + self.current_move_stone > 3:
            return False, False, 0
        self.current_move_stone += move_stone
        self.push_stone(y, x, description, line)
        return True, move_stone == 3, dropped

    def can_push_stone(self, y: int, x: int, description: HexDescription) -> (Optional[list], int, int):
        line, move_stone = self.get_line(y, x, description), 0
        if len(line) == 1:
            return None, 1, -1

        v_acc = (lambda v: line if v else None)
        lm, om, flp = 0, 0, False
        for n in line:
            if n == StoneColor.NONE.value:
                return v_acc(4 > lm > om), lm, 0
            elif n == self.game_vector[2]:
                if flp:
                    return None, 0, 0
                lm += 1
            else:
                flp = True
                om += 1
        return v_acc(4 > lm > om), lm, 1

    def push_stone(self, y: int, x: int, description: HexDescription, line: list = None) -> None:
        if line is None:
            line = self.get_line(y, x, description)

        if line[len(line) - 1] == StoneColor.BLACK.value:
            self.game_vector[3] += 1
        elif line[len(line) - 1] == StoneColor.WHITE.value:
            self.game_vector[4] += 1
        line = [0] + line.pop()
        self.set_line(y, x, description, line)

    # Bin Field Control

    def get_line(self, y: int, x: int, description: HexDescription) -> list:
        if description == HexDescription.XP:
            if y < self.edge_size:
                return [self.game_vector[5 + self.get_1d_pos(y, xp)] for xp in range(x, self.edge_size + y)]
            else:
                return [self.game_vector[5 + self.get_1d_pos(y, xp)] for xp in range(x, self.edge_size * 3 - y + x - 2)]
        elif description == HexDescription.XM:
            if y < self.edge_size:
                return [self.game_vector[5 + self.get_1d_pos(y, x - xp)] for xp in range(0, x + 1)]
            else:
                return [self.game_vector[5 + self.get_1d_pos(y, x - xp)] for xp in range(0, x - y + self.edge_size)]
        elif description == HexDescription.YP:
            if x < self.edge_size:
                return [self.game_vector[5 + self.get_1d_pos(yp, x)] for yp in range(y, self.edge_size + x)]
            else:
                return [self.game_vector[5 + self.get_1d_pos(yp, x)] for yp in range(y, self.edge_size * 2 - 1)]
        elif description == HexDescription.YM:
            if x < self.edge_size:
                return [self.game_vector[5 + self.get_1d_pos(y - yp, x)] for yp in range(0, y + 1)]
            else:
                return [self.game_vector[5 + self.get_1d_pos(y - yp, x)] for yp in range(0, y - x + self.edge_size)]
        elif description == HexDescription.ZP:
            if y < self.edge_size:
                return [self.game_vector[5 + self.get_1d_pos(yp, xp)] for yp, xp in
                        zip_longest(range(y, self.edge_size * 2 - 1), range(x, x + self.edge_size),
                                    fillvalue=self.edge_size * 2 - 1)]
            else:
                return [self.game_vector[5 + self.get_1d_pos(yp, xp)] for yp, xp in
                        zip_longest(range(y, self.edge_size * 2 - 1), range(x, x + self.edge_size),
                                    fillvalue=self.edge_size * 2 - 1)]
        elif description == HexDescription.ZM:
            if x < self.edge_size:
                return [self.game_vector[5 + self.get_1d_pos(y - yp, x - xp)] for yp, xp in
                        zip_longest(range(0, y), range(0, x),
                                    fillvalue=0)]
            else:
                return [self.game_vector[5 + self.get_1d_pos(y - yp, x - xp)] for yp, xp in
                        zip_longest(range(0, y), range(0, x),
                                    fillvalue=0)]

    def set_line(self, y: int, x: int, description: HexDescription, line: list) -> None:
        if description == HexDescription.XP:
            for index in range(len(line)):
                self.game_vector[5 + self.get_1d_pos(y, x + index)] = line[index]
        elif description == HexDescription.XM:
            for index in range(len(line)):
                self.game_vector[5 + self.get_1d_pos(y, x - index)] = line[index]
        elif description == HexDescription.YP:
            for index in range(len(line)):
                self.game_vector[5 + self.get_1d_pos(y + index, x)] = line[index]
        elif description == HexDescription.YM:
            for index in range(len(line)):
                self.game_vector[5 + self.get_1d_pos(y - index, x)] = line[index]
        elif description == HexDescription.ZP:
            for index in range(len(line)):
                self.game_vector[5 + self.get_1d_pos(y + index, x + index)] = line[index]
        elif description == HexDescription.ZM:
            for index in range(len(line)):
                self.game_vector[5 + self.get_1d_pos(y - index, x - index)] = line[index]

    def set_field_stone(self, y: int, x: int, color: StoneColor) -> None:
        self.game_vector[5 + self.get_1d_pos(y, x)] = color.value

    def get_field_stone(self, y: int, x: int) -> int:
        return self.game_vector[5 + self.get_1d_pos(y, x)]

    # Position Data

    def check_valid_pos(self, y: int, x: int) -> bool:
        if y < self.edge_size:
            return y < self.edge_size * 2 and self.edge_size + y > x > -1
        else:
            return y < self.edge_size * 2 and y - self.edge_size < x < self.edge_size * 2 - 1

    # Private

    def _flip_color(self) -> None:
        if self.game_vector[2] == StoneColor.BLACK.value:
            self.game_vector[2] = StoneColor.WHITE.value
        else:
            self.game_vector[2] = StoneColor.BLACK.value
