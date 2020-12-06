#!/usr/bin/env python3

with open("input.txt") as f:
    rows = f.read().splitlines()

print(sum(line[i * 3 % len(line)] == "#" for i, line in enumerate(rows)))
