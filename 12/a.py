#!/usr/bin/env python3

import turtle
turtle.tracer(0, 0)

actions = {
    "N": lambda v: turtle.sety(turtle.ycor() + v),
    "S": lambda v: turtle.sety(turtle.ycor() - v),
    "E": lambda v: turtle.setx(turtle.xcor() + v),
    "W": lambda v: turtle.setx(turtle.xcor() - v),
    "F": turtle.forward,
    "L": turtle.left,
    "R": turtle.right,
}

with open("input.txt") as f:
    lines = f.read().splitlines()
    orders = [(line[:1], int(line[1:])) for line in lines]

for action, value in orders:
    actions[action](value)

print(round(abs(turtle.ycor()) + abs(turtle.xcor())))
