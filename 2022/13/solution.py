#!/usr/bin/env python3
import json
from functools import cmp_to_key
from itertools import zip_longest

Packet = list[int | list]

def pair(iterable):
    args = [iter(iterable)] * 2
    return zip(*args, strict=True)

def compare(left: Packet, right: Packet):
    for left_item, right_item in zip_longest(left, right, fillvalue=None):
        if isinstance(left_item, list) and isinstance(right_item, int):
            if cmpval := compare(left_item, [right_item]):
                return cmpval
        elif isinstance(left_item, int) and isinstance(right_item, list):
            if cmpval := compare([left_item], right_item):
                return cmpval
        elif isinstance(left_item, list) and isinstance(right_item, list):
            if cmpval := compare(left_item, right_item):
                return cmpval
        elif left_item is None:
            return -1
        elif right_item is None:
            return 1
        elif left_item < right_item:
            return -1
        elif left_item > right_item:
            return 1
    return 0

with open("input.txt") as f:
    lines = f.read().splitlines()

pairs = [(left, right) for left, right in pair(json.loads(line) for line in lines if line)]

# part 1
print(sum(i + 1 for i, (left, right) in enumerate(pairs) if compare(left, right) == -1))

packets = [packet for pair in pairs for packet in pair]
packets.extend([[[2]], [[6]]])
packets.sort(key=cmp_to_key(compare))
two = packets.index([[2]]) + 1
six = packets.index([[6]]) + 1

# part 2
print(two * six)
