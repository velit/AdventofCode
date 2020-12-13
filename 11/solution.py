#!/usr/bin/env python3

def neibörinos(g, y0, x0, inf):
    vectors = (-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
    for vect_y, vect_x in vectors:
        for i in (range(1, max(len(g), len(g[y0]))) if inf else [1]):
            y = y0 + vect_y * i
            x = x0 + vect_x * i
            if 0 <= y < len(g) and 0 <= x < len(g[y]):
                if g[y][x] == "." and inf:
                    continue
                else:
                    yield g[y][x]
                    break
            else:
                break

def step(g, y, x, tolerance, inf):
    if g[y][x] == "L":
        return "#" if all(n != "#" for n in neibörinos(g, y, x, inf)) else "L"
    elif g[y][x] == "#":
        return "L" if sum(n == "#" for n in neibörinos(g, y, x, inf)) >= tolerance else "#"
    else:
        return g[y][x]

def simulate(grid, tolerance, inf):
    old_grid = []
    while grid != old_grid:
        old_grid = grid
        grid = [[step(old_grid, y, x, tolerance, inf) for x in range(len(line))]
                for y, line in enumerate(old_grid)]
    print(sum(t == "#" for line in grid for t in line))

with open("input.txt") as f:
    lines = f.read().splitlines()
    grid = [list(line) for line in lines]

simulate(grid, tolerance=4, inf=False)
simulate(grid, tolerance=5, inf=True)
