#!/usr/bin/env python3
import operator
from functools import reduce

product = lambda iterable: reduce(operator.mul, iterable, 1)

with open("input.txt") as f:
    rows = f.read().splitlines()

parts = (
    sum(line[i * 1 % len(line)] == "#" for i, line in enumerate(rows)),
    sum(line[i * 3 % len(line)] == "#" for i, line in enumerate(rows)),
    sum(line[i * 5 % len(line)] == "#" for i, line in enumerate(rows)),
    sum(line[i * 7 % len(line)] == "#" for i, line in enumerate(rows)),
    sum(line[i * 1 % len(line)] == "#" for i, line in enumerate(rows[::2]))
)

print(product(parts))
