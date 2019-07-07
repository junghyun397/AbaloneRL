import math
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
    while index < get_field_size(edge_size):
        if not edge_cut > x:
            if y < edge_size - 1:
                edge_cut += 1
            else:
                edge_cut -= 1
                shift_x += 1
            y += 1
            x = 0
        yield index, y, x + shift_x
        index += 1
        x += 1


_indexed_edge_size = (3, 5)
_indexed_pos = dict()


def _create_indexed_pos(edge_size: int) -> None:
    _indexed_pos[edge_size] = dict()
    for index, y, x in pos_generator(edge_size):
        _indexed_pos[edge_size][index] = y, x
        _indexed_pos[edge_size][y, x] = index


def _build_indexed_pos(target: tuple) -> None:
    for n in target:
        _create_indexed_pos(n)


_build_indexed_pos(_indexed_edge_size)


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
    if edge_size not in _indexed_edge_size:
        return get_pos_method(edge_size)

    temp_map = _indexed_pos[edge_size]

    def get_1d_pos(y: int, x: int) -> int:
        return temp_map[y, x]

    def get_2d_pos(index: int) -> (int, int):
        return temp_map[index]

    return get_1d_pos, get_2d_pos


# Field Generator

def new_field(size: int) -> np.ndarray:
    return np.zeros((get_field_size(size),), dtype=np.int8)


def new_vector(size: int) -> np.ndarray:
    return np.zeros((5 + get_field_size(size),), dtype=np.int8)


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

        self.current_out_black = 0
        self.current_out_white = 0

    # Bin Data

    def set_game_vector(self, vector: np.ndarray) -> None:
        self.current_out_black, self.current_out_white = 0, 0
        self.game_vector = vector

    def reset(self):
        self.game_vector = np.zeros((5 + get_field_size(self.edge_size),), dtype=np.int8)

    def copy(self):
        return AbaloneAgent(self.edge_size, np.copy(self.game_vector))

    def copy_vector(self) -> np.ndarray:
        return np.copy(self.game_vector)

    # Game Data

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

    def next_turn(self) -> (int, int, Optional[StoneColor]):
        self.game_vector[3] += self.current_out_black
        self.game_vector[4] += self.current_out_white
        temp_out_black, temp_out_white = self.current_out_black, self.current_out_white
        self.current_out_black, self.current_out_white = 0, 0

        self.game_vector[1] += 1
        self._flip_color()
        return temp_out_black, temp_out_white, self.get_winner()

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
            if s == self.game_vector[2]:
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
            self.game_vector[3] += 1
        elif line[len(line) - 1] == StoneColor.WHITE.value:
            self.game_vector[4] += 1

        line = [0] + line.pop()
        self.set_line(y, x, description, line)

    # Game Observe

    def get_winner(self) -> Optional[StoneColor]:
        if self.game_vector[4] > 5:
            return StoneColor.BLACK
        elif self.game_vector[3] > 5:
            return StoneColor.WHITE
        return None

    # Bin Field Control

    def get_line(self, y: int, x: int, description: HexDescription) -> list:
        if description == HexDescription.XP:
            if y < self.edge_size:
                return [self.game_vector[5 + self.get_1d_pos(y, xp)] for xp in range(x, self.edge_size + y - 1)]
            else:
                return [self.game_vector[5 + self.get_1d_pos(y, xp)] for xp in range(x, self.edge_size * 2 - 2)]
        elif description == HexDescription.XM:
            if y < self.edge_size:
                return [self.game_vector[5 + self.get_1d_pos(y, xp)] for xp in reversed(range(0, x))]
            else:
                return [self.game_vector[5 + self.get_1d_pos(y, xp)] for xp in
                        reversed(range(y - self.edge_size + 1, x))]
        elif description == HexDescription.YP:
            if x < self.edge_size:
                return [self.game_vector[5 + self.get_1d_pos(yp, x)] for yp in range(y, self.edge_size + x)]
            else:
                return [self.game_vector[5 + self.get_1d_pos(yp, x)] for yp in range(y, self.edge_size * 2 - 2)]
        elif description == HexDescription.YM:
            if x < self.edge_size:
                return [self.game_vector[5 + self.get_1d_pos(yp, x)] for yp in reversed(range(0, y))]
            else:
                return [self.game_vector[5 + self.get_1d_pos(yp, x)] for yp in
                        reversed(range(x - self.edge_size + 1, x))]
        elif description == HexDescription.ZP:
            return [self.game_vector[5 + self.get_1d_pos(yp, xp)] for yp, xp in
                    zip(range(y, self.edge_size * 2 - 2), range(x, self.edge_size * 2 - 2))]
        elif description == HexDescription.ZM:
            return [self.game_vector[5 + self.get_1d_pos(yp, xp)] for yp, xp in
                    zip(reversed(range(0, y)), reversed(range(0, x)))]

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
