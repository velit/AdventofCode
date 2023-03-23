#!/usr/bin/env python3
from collections.abc import Iterable
from dataclasses import field, dataclass
from itertools import product

from common.coord import Position

@dataclass
class Mountain:
    unevaluated: set[Position] = field(default_factory=lambda: set(Position(*pos) for pos in product(*[range(20)] * 3)))
    cubes: set[Position] = field(default_factory=set)
    faces = 0

    def fill_cube(self, cube: Position):
        cube_neighbours = neighbour_amount(self.cubes, cube)
        self.faces += 6 - cube_neighbours * 2
        self.cubes.add(cube)
        self.unevaluated.remove(cube)

neighbour_positions = (
    Position(-1, 0, 0),
    Position(0, -1, 0),
    Position(0, 0, -1),
    Position(0, 0, 1),
    Position(0, 1, 0),
    Position(1, 0, 0),
)

def neighbours(origin: Position) -> Iterable[Position]:
    for neighbour_direction in neighbour_positions:
        yield origin + neighbour_direction

def neighbour_amount(positions: set[Position], origin: Position) -> int:
    return sum(1 for neighbour in neighbours(origin) if neighbour in positions)

def main() -> None:
    with open("input.txt") as f:
        cube_list = [Position(int(x), int(y), int(z)) for x, y, z in (line.split(",") for line in f.read().splitlines())]
    m = Mountain()
    for cube in cube_list:
        m.fill_cube(cube)

    # part 1
    print(m.faces)

    while m.unevaluated:
        stack = [next(iter(m.unevaluated))]
        current_set = {stack[0]}
        inside = True

        while stack:
            current = stack.pop()
            empty_neighbours = (pos for pos in neighbours(current) if pos not in current_set and pos not in m.cubes)
            for neighbor in empty_neighbours:
                if neighbor not in m.unevaluated:
                    inside = False
                    continue
                current_set.add(neighbor)
                stack.append(neighbor)

        if inside:
            for cube in current_set:
                m.fill_cube(cube)
        m.unevaluated -= current_set

    # part 2
    print(m.faces)

if __name__ == "__main__":
    main()
