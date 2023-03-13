#!/usr/bin/env python3
from __future__ import annotations

from collections.abc import Iterable

from common.coord import Coord

directions = {
    "D": Coord(+1, +0),
    "R": Coord(+0, +1),
    "U": Coord(-1, +0),
    "L": Coord(+0, -1),
}

def sign(n: int) -> int:
    if n > 0:
        return 1
    elif n < 0:
        return -1
    return 0

with open("input.txt") as f:
    lines = f.read().splitlines()
    instructions = [(directions[dir_], int(count)) for dir_, count in (line.split() for line in lines)]

def simulate_rope(instructions: Iterable[tuple[Coord, int]], length: int) -> int:
    rope = [Coord() for _ in range(length)]
    visited = {rope[-1]}

    for direction, count in instructions:
        for _ in range(count):
            rope[0] += direction

            for i in range(1, length):
                y_diff = rope[i - 1].y - rope[i].y
                x_diff = rope[i - 1].x - rope[i].x

                if abs(y_diff) < 2 and abs(x_diff) < 2:
                    y_diff, x_diff = 0, 0
                else:
                    if abs(y_diff) == 2:
                        y_diff -= sign(y_diff)  # reduce 1 from magnitude
                    if abs(x_diff) == 2:
                        x_diff -= sign(x_diff)

                rope[i] += Coord(y_diff, x_diff)
            visited.add(rope[-1])
    return len(visited)

print(simulate_rope(instructions, 2))
print(simulate_rope(instructions, 10))
