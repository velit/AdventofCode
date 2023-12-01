#!/usr/bin/env python3
import re
from dataclasses import dataclass

from common.coord import Coord
from common.dimensions import Dimensions
from common.table import Table

dirs = (
    Coord(0, 1),
    Coord(1, 0),
    Coord(0, -1),
    Coord(-1, 0),
)

dir_i = {
    "R": 1,
    "L": -1,
}

@dataclass
class Roguelike:
    table: Table[str]
    coord = Coord(0, 0)
    direction_i = 0

    def __post_init__(self):
        self.move()

    @property
    def direction(self):
        return dirs[self.direction_i % len(dirs)]

    def turn(self, side: str):
        self.direction_i += dir_i[side]

    def move(self):
        new_coord, item = self._get_from_direction()
        if item == ".":
            self.coord = new_coord

    def _wrap_coord(self, coord: Coord) -> Coord:
        rows, cols = self.table.dimensions
        return Coord(coord.y % rows, coord.x % cols)

    def _get_from_direction(self) -> tuple[Coord, str]:
        coord_run = self._wrap_coord(self.coord + self.direction)
        while (item := self.table[self._wrap_coord(coord_run)]) == " ":
            coord_run = self._wrap_coord(coord_run + self.direction)
        return coord_run, item

    def __str__(self):
        cur = self.table[self.coord]
        self.table[self.coord] = ">v<^"[self.direction_i % 4]
        table_str = str(self.table)
        self.table[self.coord] = cur
        return table_str

def main() -> None:
    with open("input.txt") as f:
        map_str: str
        map_str, instruction_str = f.read().split("\n\n")
    cols = len(max(map_str.splitlines(), key=len))
    map_lines = [line.ljust(cols) for line in map_str.splitlines()]
    rows = len(map_lines)

    table = Table(Dimensions(rows, cols), "".join(map_lines))
    instructions = re.findall(r"\d+|[RL]", instruction_str)
    rl = Roguelike(table)

    for instruction in instructions:
        match instruction:
            case "R" | "L" as side:
                rl.turn(side)
            case number:
                for _ in range(int(number)):
                    rl.move()

    print(1000 * (rl.coord.y + 1) + 4 * (rl.coord.x + 1) + rl.direction_i % 4)

if __name__ == "__main__":
    main()
