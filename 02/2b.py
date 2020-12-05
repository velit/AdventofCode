#!/usr/bin/env python3
import re

with open("input.txt") as f:
    inputs = f.readlines()

# Split the input lines into a, b, char and password tokens
parsed_data = (re.split(r": |[- ]", row) for row in inputs)

def password_policy(a, b, char, password):
    first = password[int(a) - 1]
    second = password[int(b) - 1]
    return (char == first) ^ (char == second)

print(len([1 for args in parsed_data if password_policy(*args)]))
