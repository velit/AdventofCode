#!/usr/bin/env python3

from itertools import combinations

with open("input.txt") as f:
    nums = [int(n) for n in f.read().splitlines()]

preamble = 25
invalid = next(nums[i] for i in range(preamble, len(nums))
               if nums[i] not in map(sum, combinations(nums[i - preamble:i], 2)))
print(invalid)

counter = 0
i = 0
j = 0

while counter != invalid:
    counter += nums[j]
    j += 1
    if counter > invalid:
        counter = 0
        i += 1
        j = i

encr_rang = nums[i:j]
print(min(encr_rang) + max(encr_rang))
