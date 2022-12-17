#!/usr/bin/env python3

with open("input.txt") as f:
    lines = f.read().splitlines()

elves_raw = []
items = []
for line in lines:
    if not line:
        elves_raw.append(items)
        items = []
        continue
    items.append(int(line))

elves = [sum(elf) for elf in elves_raw]

print(max(elves))
elves.sort()
print(sum(elves[-3:]))

