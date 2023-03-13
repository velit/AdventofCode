#!/usr/bin/env python3
from collections.abc import Iterable, Callable
from functools import partial
from heapq import heappush, heappop

from common.coord import Coord
from common.table import Table
from common.dimensions import Dimensions
from common.util import manhattan_distance

NeighborCall = Callable[[Coord], Iterable[tuple[Coord, int]]]
HeuristicCall = Callable[[Coord, Coord], int]

def char_to_depth(char: str) -> int:
    if char == "S":
        return char_to_depth("a")
    if char == "E":
        return char_to_depth("z")
    return ord(char) - ord("a") + 1

def height_neighbors(table: Table[int], coord: Coord) -> Iterable[tuple[Coord, int]]:
    orthogonals = Coord(-1, 0), Coord(1, 0), Coord(0, -1), Coord(0, 1)
    height = table[coord]
    for direction in orthogonals:
        neighbor = coord + direction
        if not table.is_legal(neighbor):
            continue
        neighbor_height = table[neighbor]
        if height <= neighbor_height + 1:
            yield neighbor, 1

def a_star(start: Coord, goal: Coord, neighbors: NeighborCall, heuristic: HeuristicCall) -> Iterable[Coord]:
    _start, _goal = goal, start
    came_from: dict[Coord, Coord] = {}
    closed_set = set()
    open_member = set()
    open_member.add(_start)

    cheap = {_start: 0}  # Current cheapest cost to coord
    open_prio: list[tuple[int, Coord]] = []
    heappush(open_prio, (0, _start))

    while open_prio:
        if open_prio[0][1] == _goal:
            break
        origin = heappop(open_prio)[1]
        if origin not in closed_set:
            open_member.remove(origin)
            closed_set.add(origin)

            for node, cost in neighbors(origin):
                if node not in closed_set and (node not in open_member or cheap[origin] + cost < cheap[node]):
                    came_from[node] = origin
                    cheap[node] = cheap[origin] + cost
                    estimate = cheap[node] + heuristic(node, _goal)
                    heappush(open_prio, (estimate, node))
                    open_member.add(node)
    else:
        raise ValueError(f"No possible paths between {start=} and {goal=}")

    cur = start
    while cur != goal:
        cur = came_from[cur]
        yield cur

def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    start = next(Coord(row, col) for row, line in enumerate(lines) for col, char in enumerate(line) if char == "S")
    starts = [Coord(row, col) for row, line in enumerate(lines) for col, char in enumerate(line) if char == "a"]
    goal  = next(Coord(row, col) for row, line in enumerate(lines) for col, char in enumerate(line) if char == "E")
    dimensions = Dimensions(len(lines), len(lines[0]))
    table = Table(dimensions, (char_to_depth(char) for line in lines for char in line))
    # print(table)

    route = list(a_star(start, goal, partial(height_neighbors, table), manhattan_distance))
    # part 1
    print(len(route))
    route_lens = []
    start_size = len(starts)
    print(f"{start_size=}")
    for i, start in enumerate(starts):
        try:
            route_lens.append(len(tuple(a_star(start, goal, partial(height_neighbors, table), manhattan_distance))))
        except ValueError:
            pass
        print(f"\r{start}", end="", flush=True)
    print()
    # part 2
    print(min(route_lens))

if __name__ == '__main__':
    main()
