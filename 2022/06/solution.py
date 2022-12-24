#!/usr/bin/env python3

with open("input.txt") as f:
    cypher = f.read().splitlines()[0]

def find_unique_sequence(cypher: str, length: int):
    for i in range(len(cypher) - length - 1):
        window = cypher[i:i + length]
        if len(set(window)) == length:
            print(i + length)
            break
    else:
        print("Not found")

find_unique_sequence(cypher, 4)
find_unique_sequence(cypher, 14)