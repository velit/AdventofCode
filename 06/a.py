#!/usr/bin/env python3

with open("input.txt") as f:
    groups = f.read().split("\n\n")

print(sum(len(set("".join(group.split()))) for group in groups))
