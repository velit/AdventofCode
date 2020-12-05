#!/usr/bin/env python3
import re
from collections import Counter

with open("input.txt") as f:
    inputs = f.readlines()

# Split the input lines into min, max char and password tokens
parsed_data = (re.split(r": |[- ]", row) for row in inputs)

print(len([1 for (min, max, char, passw) in parsed_data
           if int(min) <= Counter(passw)[char] <= int(max)]))
