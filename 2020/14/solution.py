#!/usr/bin/env python3

import re
import itertools

with open("input.txt") as f:
    inputs = f.read().splitlines()

def get_masks(line):
    full_mask, = re.fullmatch(r"mask = (.+)", line).groups()
    zero_mask = int(full_mask.replace("X", "1"), 2)
    one_mask = int(full_mask.replace("X", "0"), 2)
    return zero_mask, one_mask

def get_x_indexes(line):
    return [i for i, char in enumerate(reversed(line)) if char == "X"]

def get_mem_values(line):
    i, value = re.fullmatch(r"mem\[(\d+)\] = (\d+)", line).groups()
    return int(i), int(value)


mem1 = {}
for line in inputs:
    if line.startswith("mask"):
        zero_mask, one_mask = get_masks(line)
    if line.startswith("mem"):
        i, value = get_mem_values(line)
        value |= one_mask
        value &= zero_mask
        mem1[i] = value

print(sum(mem1.values()))

mem2 = {}
for line in inputs:
    if line.startswith("mask"):
        zero_mask, one_mask = get_masks(line)
        x_indexes = get_x_indexes(line)
    if line.startswith("mem"):
        mem_i, value = get_mem_values(line)
        mem_i |= one_mask
        # X variations
        for variation in itertools.product((0, 1), repeat=len(x_indexes)):
            for bit_i, bit in zip(x_indexes, variation):
                # Set 'bit_i'th bit to 'bit' value
                mem_i ^= (-bit ^ mem_i) & (1 << bit_i);
            mem2[mem_i] = value

print(sum(mem2.values()))
