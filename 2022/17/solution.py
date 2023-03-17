#!/usr/bin/env python3
from collections.abc import Sequence, Callable
from copy import deepcopy
from dataclasses import field, dataclass, InitVar
from typing import ClassVar

from common.coord import Coord
from common.dimensions import Dimensions
from common.table import Table

DOWN = Coord(-1, 0)
LEFT = Coord(0, -1)
RIGHT = Coord(0, 1)

def horizontal_line(top_left: Coord) -> Sequence[Coord]:
    return [top_left + Coord(0, x) for x in range(4)]

def cross(top_left: Coord) -> Sequence[Coord]:
    return [
        top_left + Coord(0, 1),
        top_left + Coord(1, 0),
        top_left + Coord(1, 1),
        top_left + Coord(1, 2),
        top_left + Coord(2, 1),
    ]

def l_block(top_left: Coord) -> Sequence[Coord]:
    return [
        top_left + Coord(0, 0),
        top_left + Coord(0, 1),
        top_left + Coord(0, 2),
        top_left + Coord(1, 2),
        top_left + Coord(2, 2),
    ]

def vertical_line(top_left: Coord) -> Sequence[Coord]:
    return [top_left + Coord(y, 0) for y in range(4)]

def square(top_left: Coord) -> Sequence[Coord]:
    return [
        top_left + Coord(0, 0),
        top_left + Coord(0, 1),
        top_left + Coord(1, 0),
        top_left + Coord(1, 1),
    ]

def init_table() -> Table[str]:
    table = Table(Dimensions(1, 9), fill_value=".")
    table[0, 0] = table[0, 8] = "+"
    for i in range(7):
        table[0, 1 + i] = "-"
    return table

@dataclass
class Tetris:

    initial_height: InitVar[int]
    directions: Sequence[Coord]
    dir_total: int = 0
    sprite_total: int = 0
    sprite_coord: Coord = Coord(4, 3)
    table: Table[str] = field(default_factory=init_table)
    floor_row: int = 0

    sprites: ClassVar[list[Callable[[Coord], Sequence[Coord]]]] = [
        horizontal_line,
        cross,
        l_block,
        vertical_line,
        square,
    ]

    def __post_init__(self, initial_height: int):
        self.increase(initial_height - 1)

    @property
    def dir_i(self) -> int:
        return self.dir_total % len(self.directions)

    def get_gas_direction_and_increment(self) -> Coord:
        direction = self.directions[self.dir_i]
        self.dir_total += 1
        return direction

    @property
    def sprite_i(self) -> int:
        return self.sprite_total % len(self.sprites)

    @property
    def current_sprite(self) -> Sequence[Coord]:
        return self.get_sprite(self.sprite_coord)

    def get_sprite(self, coord: Coord) -> Sequence[Coord]:
        return self.sprites[self.sprite_i](coord)

    def sprite_can_fit(self, direction: Coord):
        sprite = self.get_sprite(self.sprite_coord + direction)
        return all(self.table[coord] == "." for coord in sprite)

    def move_sprite(self, direction: Coord):
        self.sprite_coord += direction

    def increase(self, amount: int):
        new_row = self.table.rows
        self.table.increase_first_dimension(amount, fill_value=".")
        for y in range(amount):
            self.table[new_row + y, 0] = "|"
            self.table[new_row + y, 8] = "|"

    def solidify_sprite(self, char="#"):
        highest_y = self.solidify_table(self.table, self.current_sprite, char)
        self.floor_row = max(self.floor_row, highest_y)
        self.sprite_total += 1
        self.sprite_coord = Coord(self.floor_row + 4, 3)
        self.increase(7 - (self.table.rows - 1 - self.floor_row))

    def print_unsolidified(self):
        """Print the table with the current sprite without modifying the table."""
        print_table = deepcopy(self.table)
        self.solidify_table(print_table, self.current_sprite, "@")
        print(print_table.str_row_inverted())
        print()

    @classmethod
    def solidify_table(cls, table: Table[str], sprite: Sequence[Coord], char="#") -> int:
        """Returns the new highest coord"""
        highest = max(sprite, key=lambda coord: coord.y)
        for coord_ in sprite:
            table[coord_] = char
        return highest.y


dirs = {
    ">": RIGHT,
    "<": LEFT,
}

def main(n, cycle_detect=False):
    with open("input.txt") as f:
        directions = [dirs[char] for char in f.read().splitlines()[0]]

    tetris = Tetris(7, directions)
    cycles = {}
    streak = 0
    additional_cycles_required = None
    while tetris.sprite_total < n:

        gas_dir = tetris.get_gas_direction_and_increment()
        if tetris.sprite_can_fit(gas_dir):
            tetris.move_sprite(gas_dir)

        if tetris.sprite_can_fit(DOWN):
            tetris.move_sprite(DOWN)
            continue

        tetris.solidify_sprite()

        if not cycle_detect:
            continue

        key = (tetris.dir_i, tetris.sprite_i, tetris.sprite_coord.x)
        previous = cycles.get(key, None)
        cycles[key] = {"dir": tetris.dir_total, "sprite": tetris.sprite_total, "floor": tetris.floor_row}

        if additional_cycles_required is not None:
            if additional_cycles_required > 0:
                additional_cycles_required -= 1
            else:
                sprites_per_cycle = cycles[key]["sprite"] - previous["sprite"]
                repeat_cycles = n // sprites_per_cycle
                floors_per_cycle = (cycles[key]["floor"] - previous["floor"])
                print(floors_per_cycle * repeat_cycles + previous["floor"])
                break
            continue

        if previous:
            streak += 1
            print(f"{key=}")
            print(f"Previous totals {previous}")
            print(f"Current totals  {cycles[key]}")
        else:
            streak = 0

        if streak > len(cycles) // 2:
            print("More than 50% of data is now duplicate states")
            sprites_per_cycle = cycles[key]["sprite"] - previous["sprite"]
            base = previous["sprite"]
            repeat_cycles = n // sprites_per_cycle
            additional_cycles_required = n - (base + repeat_cycles * sprites_per_cycle) - 1

    print(tetris.floor_row)

if __name__ == '__main__':
    main(2022)
    main(1000000000000, cycle_detect=True)
