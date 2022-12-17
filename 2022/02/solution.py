#!/usr/bin/env python3

with open("input.txt") as f:
    lines = f.read().splitlines()

score_lookup1 = {
    "B X": 1,
    "C Y": 2,
    "A Z": 3,
    "A X": 4,
    "B Y": 5,
    "C Z": 6,
    "C X": 7,
    "A Y": 8,
    "B Z": 9,
}

score_lookup2 = {
    "B X": 1,
    "C X": 2,
    "A X": 3,
    "A Y": 4,
    "B Y": 5,
    "C Y": 6,
    "C Z": 7,
    "A Z": 8,
    "B Z": 9,
}

print(sum(score_lookup1[line] for line in lines))
print(sum(score_lookup2[line] for line in lines))
