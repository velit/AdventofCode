#!/usr/bin/env python3

import re

def parse(line):
    bag, contain = re.match(r"(.+) bags contain (.+)\.", line).groups()
    if contain == "no other bags": return bag, []
    return bag, [re.match(r"(\d) (.+) bags?", child).groups() for child in contain.split(", ")]

def contains_needle(bags, bag, needle):
    return any(child == needle or contains_needle(bags, child, needle) for _, child in bags[bag])

def count(bags, bag, mult):
    return mult + mult * sum(count(bags, child, int(c_mult)) for c_mult, child in bags[bag])

with open("input.txt") as f:
    lines = f.read().splitlines()
bags = dict(parse(line) for line in lines)

print(sum(contains_needle(bags, bag, "shiny gold") for bag in bags))
print(count(bags, "shiny gold", 1) - 1)
