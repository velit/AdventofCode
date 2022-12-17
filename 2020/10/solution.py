#!/usr/bin/env python3

from collections import Counter
from itertools import tee

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

with open("input.txt") as f:
    nums = [int(n) for n in f.read().splitlines()]
    nums.append(0)
    nums.append(max(nums) + 3)
    nums.sort()

one = 0
three = 0
for a, b in pairwise(nums):
    if b - a == 1:
        one += 1
    elif b - a == 3:
        three += 1
print(one * three)

lookup = {1: 2**0, 2: 2**1, 3: 2**2, 4: 2**3 - 1, 5: 2**4 - 3}
combinations = 1
chain = 0
for a, b in pairwise(nums):
    if b - a == 1:
        chain += 1
    elif chain > 0:
        combinations *= lookup[chain]
        chain = 0

print(combinations)
