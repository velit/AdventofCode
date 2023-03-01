#!/usr/bin/env python3
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from itertools import product
from math import prod

DOWN = (1, 0)
RIGHT = (0, 1)
UP = (-1, 0)
LEFT = (0, -1)


@dataclass
class Tree:
    height: int
    is_visible: bool = False
    scenic_score: int = 0

with open("input.txt") as f:
    lines = f.read().splitlines()

forest = [[Tree(int(digit)) for digit in line] for line in lines]

def mark_bidirectional_visibility(line: Iterable[Tree]) -> None:
    line_list = list(line)
    current = -1
    for tree in line_list:
        if tree.height > current:
            tree.is_visible = True
            current = tree.height
    current = -1
    for tree in reversed(line_list):
        if tree.height > current:
            tree.is_visible = True
            current = tree.height

def slice_forest(forest: list[list[Tree]], start: tuple[int, int], direction: tuple[int, int]) -> Iterator[Tree]:
    y_start, x_start = start
    y_stop = y_start + 1
    x_stop = x_start + 1
    if direction == DOWN:
        for y in range(y_start, len(forest)):
            yield forest[y][x_start]
    elif direction == RIGHT:
        for x in range(x_start, len(forest[y_start])):
            yield forest[y_start][x]
    elif direction == UP:
        for y in reversed(range(0, y_stop)):
            yield forest[y][x_start]
    elif direction == LEFT:
        for x in reversed(range(0, x_stop)):
            yield forest[y_start][x]
    else:
        assert False, f"Unhandled {direction=}"

def calculate_scenic_score(forest: list[list[Tree]], start: tuple[int, int]) -> None:
    y, x = start
    tree = forest[y][x]
    directions = UP, DOWN, LEFT, RIGHT
    distances = map(lambda direction: calculate_view_distance(slice_forest(forest, start, direction)), directions)
    tree.scenic_score = prod(distances)

def calculate_view_distance(tree_slice: Iterator[Tree]) -> int:
    tree = next(tree_slice)
    distance = 0
    for other_tree in tree_slice:
        distance += 1
        if other_tree.height >= tree.height:
            break
    return distance

def iter_forest(forest: list[list[Tree]]) -> Iterator[tuple[int, int]]:
    return product(range(len(forest)), range(len(forest[0])))


for y in range(len(forest)):
    mark_bidirectional_visibility(slice_forest(forest, (y, 0), (0, 1)))

for x in range(len(forest[0])):
    mark_bidirectional_visibility(slice_forest(forest, (0, x), (1, 0)))

# part 1
print(sum(1 for row in forest for tree in row if tree.is_visible))

for y, x in iter_forest(forest):
    calculate_scenic_score(forest, (y, x))

# part 2
print(max((forest[y][x] for y, x in iter_forest(forest)), key=lambda tree: tree.scenic_score))
