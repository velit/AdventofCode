#!/usr/bin/env python3
from common.util import grouper

with open("input.txt") as f:
    lines = f.read().splitlines()
    rucksacks = [(line[:len(line) // 2], line[len(line) // 2:]) for line in lines]

def char_priority(char: str) -> int:
    if ord(char) < ord("a"):
        return ord(char) - ord("A") + 27
    return ord(char) - ord("a") + 1

print(sum(char_priority((set(first) & set(second)).pop()) for (first, second) in rucksacks))
print(sum(char_priority((set(first) & set(second) & set(third)).pop()) for (first, second, third) in grouper(lines, 3)))
