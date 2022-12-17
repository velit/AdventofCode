#!/usr/bin/env python3

from itertools import combinations

with open("input.txt") as f:
    nums = [int(n) for n in f.read().splitlines()]

invalid = next(nums[i] for i in range(25, len(nums))
               if nums[i] not in map(sum, combinations(nums[i - 25:i], 2)))
print(invalid)

counter = j = i = 0
while counter != invalid:
    counter += nums[j]
    j += 1
    if counter > invalid:
        counter = 0
        j = i = i + 1

print(min(nums[i:j]) + max(nums[i:j]))
