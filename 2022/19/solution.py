#!/usr/bin/env python3
import re
from dataclasses import dataclass

@dataclass
class Blueprint:
    id: int
    ore_robot_ore_cost: int
    clay_robot_ore_cost: int
    obsidian_robot_ore_cost: int
    obsidian_robot_clay_cost: int
    geode_robot_ore_cost: int
    geode_robot_obsidian_cost: int

line_pattern = re.compile(r"Blueprint (\d+): Each ore robot costs (\d+) ore. "
                          r"Each clay robot costs (\d+) ore. "
                          r"Each obsidian robot costs (\d+) ore and (\d+) clay. "
                          r"Each geode robot costs (\d+) ore and (\d+) obsidian.")


def main() -> None:
    with open("input.txt") as f:
        blueprints = [Blueprint(*map(int, re.match(line_pattern, line).groups())) for line in f.read().splitlines()]
    print(blueprints)

if __name__ == "__main__":
    main()
