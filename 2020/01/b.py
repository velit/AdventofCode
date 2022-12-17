#!/usr/bin/env python3
from itertools import combinations

with open("input.txt") as f:
    numbers = [int(item) for item in f.read().splitlines()]

print(next(a*b*c for a, b, c in combinations(numbers, 3) if a + b + c == 2020))

