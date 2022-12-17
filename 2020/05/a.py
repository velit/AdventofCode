#!/usr/bin/env python3

def id(bpass):
    row = int(bpass[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(bpass[7:].replace("L", "0").replace("R", "1"), 2)
    return row * 8 + col

with open("input.txt") as f:
    passes = f.read().splitlines()

print(max(id(bpass) for bpass in passes))
