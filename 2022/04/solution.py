#!/usr/bin/env python3

with open("input.txt") as f:
    lines = f.read().splitlines()
    pairs_raw = [(first.split("-"), second.split("-")) for (first, second) in (line.split(",") for line in lines)]
    pairs = [(int(first_low), int(first_high), int(second_low), int(second_high))
             for ((first_low, first_high), (second_low, second_high)) in pairs_raw]

def enclosed(first_low, first_high, second_low, second_high):
    first = set(range(first_low, first_high + 1))
    second = set(range(second_low, second_high + 1))
    return first <= second or second <= first

def overlap(first_low, first_high, second_low, second_high):
    return set(range(first_low, first_high + 1)) & set(range(second_low, second_high + 1))

print(sum(1 for pair in pairs if enclosed(*pair)))
print(sum(1 for pair in pairs if overlap(*pair)))
