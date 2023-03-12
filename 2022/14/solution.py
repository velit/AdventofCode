#!/usr/bin/env python3
from itertools import pairwise

from common.table import Table, Dimensions


def main(part2: bool = False) -> None:
    with open("input.txt") as f:
        lines = (line.split(" -> ") for line in f.read().splitlines())
        lines = ((coord.split(",") for coord in line) for line in lines)
        lines = [[(int(y), int(x)) for x, y in line] for line in lines]

    if not part2:
        y_limit = max(y for line in lines for y, x in line) + 1
    else:
        y_limit = max(y for line in lines for y, x in line) + 3

    x_limit = max(max(x for line in lines for y, x in line) + 1, 501 + y_limit)
    table: Table[str] = Table(Dimensions(y_limit, x_limit), fillvalue=".")
    for line in lines:
        for coord_a, coord_b in pairwise(line):
            a_y, a_x = coord_a
            b_y, b_x = coord_b
            if a_x == b_x:
                for y in range(min(a_y, b_y), max(a_y, b_y) + 1):
                    table[y, a_x] = "#"
            elif a_y == b_y:
                for x in range(min(a_x, b_x), max(a_x, b_x) + 1):
                    table[a_y, x] = "#"
    table[0, 500] = "+"

    if part2:
        for x in range(x_limit):
            table[y_limit - 1, x] = "#"

    sand = 0
    try:
        while True:
            cur_y, cur_x = 0, 500
            while True:
                if table[cur_y + 1, cur_x] == ".":
                    cur_y += 1
                elif table[cur_y + 1, cur_x - 1] == ".":
                    cur_y += 1
                    cur_x -= 1
                elif table[cur_y + 1, cur_x + 1] == ".":
                    cur_y += 1
                    cur_x += 1
                else:
                    table[cur_y, cur_x] = "o"
                    sand += 1
                    assert cur_y != 0 or cur_x != 500
                    break
    except (IndexError, AssertionError):
        pass
    print(sand)

if __name__ == '__main__':
    main()
    main(part2=True)
