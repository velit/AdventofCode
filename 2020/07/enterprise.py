#!/usr/bin/env python3

import re

def parse(line):
    bag, contain = re.match(r"(.+) bags contain (.+)\.", line).groups()
    if contain == "no other bags":
        return bag, []
    return bag, [parse_contained_bag(bag_string) for bag_string in contain.split(", ")]

def parse_contained_bag(bag_string):
    number, child_bag = re.match(r"(\d) (.+) bags?", bag_string).groups()
    return child_bag, int(number)

def calc_bag_color_count(bags, original_bag):

    cache = {}
    def can_contain_bag(bag):
        if bag in cache:
            return cache[bag]

        if any(child_bag == original_bag or can_contain_bag(child_bag)
               for child_bag, _ in bags[bag]):
            cache[bag] = True
            return True

        cache[bag] = False
        return False

    return sum(can_contain_bag(bag) for bag in bags)

def child_count(bags, original_bag):

    def count(bag, mult):
        return mult + mult * sum(count(child, c_mult) for child, c_mult in bags[bag])

    return count(original_bag, 1) - 1


with open("input.txt") as f:
    lines = f.read().splitlines()
bags = dict(parse(line) for line in lines)

print(calc_bag_color_count(bags, "shiny gold"))
print(child_count(bags, "shiny gold"))
