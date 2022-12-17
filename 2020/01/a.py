#!/usr/bin/env python3
from itertools import combinations

with open("input.txt") as f:
    numbers = [int(item) for item in f.read().splitlines()]

print(next(a*b for a, b in combinations(numbers, 2) if a + b == 2020))

