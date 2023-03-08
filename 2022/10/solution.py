#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass

with open("input.txt") as f:
    instructions = [line.split() for line in f.read().splitlines()]

@dataclass(frozen=True)
class State:
    x: int

    def __init__(self, x: str | int):
        super().__setattr__("x", int(x))

    def __add__(self, other: State) -> State:
        return State(self.x + other.x)

last = State(1)
states = [last]
for instruction in instructions:
    match instruction:
        case ["noop"]:
            states.append(last)
        case ["addx", num]:
            states.append(last)
            last += State(num)
            states.append(last)
        case _:
            assert False, "You Suck"

# part 1
print(sum(map(lambda c: c * states[c - 1].x, [20, 60, 100, 140, 180, 220])))

# part 2

image = ""
for cycle, state in enumerate(states):
    if cycle and cycle % 40 == 0:
        image += "\n"
    image += "#" if state.x - 1 <= cycle % 40 <= state.x + 1 else "."

print(image)
