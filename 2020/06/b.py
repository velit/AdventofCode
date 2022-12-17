#!/usr/bin/env python3

from collections import Counter

def group_sum(group):
    people = len(group.split())
    totals = Counter("".join(group.split()))
    return sum(1 for t in totals.values() if t == people)

with open("input.txt") as f:
    groups = f.read().split("\n\n")

print(sum(group_sum(group) for group in groups))
