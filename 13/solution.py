#!/usr/bin/env python3

from math import ceil, gcd

with open("input.txt") as f:
    inputs = f.read().splitlines()

ready_time = int(inputs[0])
buses = (int(c) for c in inputs[1].split(",") if c != "x")
min_wait, min_bus = min((ceil(ready_time / bus) * bus % ready_time, bus) for bus in buses)
print("P1", min_wait * min_bus)

not_synced_buses = {int(c): offset for offset, c in enumerate(inputs[1].split(",")) if c != "x"}
t = -1
step = 1
while not_synced_buses:
    t += step
    synced_buses = [bus for bus, offset in not_synced_buses.items() if (t + offset) % bus == 0]
    for bus in synced_buses:
        del not_synced_buses[bus]
        step *= bus // gcd(step, bus)

print("P2", t)
