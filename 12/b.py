#!/usr/bin/env python3

import turtle

boat = turtle.Turtle()
wp = turtle.Turtle()
wp.setpos(10, 1)
turtle.tracer(0, 0)

actions = {
    "N": lambda v: wp.sety(wp.ycor() + v),
    "S": lambda v: wp.sety(wp.ycor() - v),
    "E": lambda v: wp.setx(wp.xcor() + v),
    "W": lambda v: wp.setx(wp.xcor() - v),
    "L": lambda v: wp.setpos(wp.pos().rotate(v)),
    "R": lambda v: wp.setpos(wp.pos().rotate(-v)),
    "F": lambda v: boat.setpos(boat.pos() + v * wp.pos()),
}

with open("input.txt") as f:
    lines = f.read().splitlines()
    orders = [(line[:1], int(line[1:])) for line in lines]

for action, value in orders:
    actions[action](value)

print(round(abs(boat.ycor()) + abs(boat.xcor())))
