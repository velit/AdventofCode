#!/usr/bin/env python3
import re

line_pattern = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

with open("input.txt") as f:
    data = [tuple(map(int, re.match(line_pattern, line).groups())) for line in f.read().splitlines()]

def manhattan_distance(ax, ay, bx, by):
    return abs(ax - bx) + abs(ay - by)

def merged(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    merged = []

    prev_start = None
    prev_limit = None
    for start, limit in sorted(ranges):
        if prev_start is prev_limit is None:
            prev_start = start
            prev_limit = limit
        elif start <= prev_limit:
            if prev_limit < limit:
                prev_limit = limit
        else:
            merged.append((prev_start, prev_limit))
            prev_start = start
            prev_limit = limit
    if prev_start is not None and prev_limit is not None:
        merged.append((prev_start, prev_limit))
    return merged

def part1(row):
    ranges = []

    beacons = set()
    for sensor_x, sensor_y, beacon_x, beacon_y in data:
        dist = manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y)
        gold_row_dist = dist - manhattan_distance(0, row, 0, sensor_y)
        if gold_row_dist >= 0:
            intersection_x_start = sensor_x - gold_row_dist
            intersection_x_limit = sensor_x + 1 + gold_row_dist
            ranges.append((intersection_x_start, intersection_x_limit))
            if beacon_y == row and intersection_x_start <= beacon_x < intersection_x_limit:
                beacons.add((beacon_x, beacon_y))

    merged_ranges = merged(ranges)

    print(sum(limit - start for start, limit in merged_ranges) - len(beacons))

space_limit = 4000000

def part2(row):
    ranges = []

    for sensor_x, sensor_y, beacon_x, beacon_y in data:
        dist = manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y)
        gold_row_dist = dist - manhattan_distance(0, row, 0, sensor_y)
        intersection_x_start = sensor_x - gold_row_dist
        intersection_x_limit = sensor_x + 1 + gold_row_dist
        if gold_row_dist >= 0 and intersection_x_start <= space_limit and intersection_x_limit > 0:
            if intersection_x_start < 0:
                intersection_x_start = 0
            if intersection_x_limit > space_limit:
                intersection_x_limit = space_limit
            ranges.append((intersection_x_start, intersection_x_limit))

    merged_ranges = merged(ranges)

    if merged_ranges != [(0, space_limit)]:
        return merged_ranges
    return None


# part1(10)
part1(2000000)

for row in range(space_limit):
    if row % 4000 == 0:
        print(f"\r{row / space_limit:.1%}", end="", flush=True)
    if ranges := part2(row):
        print(f"\r{row / space_limit:.2%}")
        print(f"{row=}, {ranges=}")
        print(row + space_limit * ranges[0][1])
        break
