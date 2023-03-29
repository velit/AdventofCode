#!/usr/bin/env python3
import operator
from collections import Counter
from collections.abc import Callable
from dataclasses import dataclass
from functools import partial
from math import prod

from common.util import all_after


@dataclass(eq=False)
class Monkeh:
    items: list[int]
    operation: Callable[[int], int]
    divisible_by: int
    true_throw: int
    false_throw: int

def parse_monkeh(lines: list[str], i: int) -> Monkeh:
    # monkey_index = int(after(lines[i].replace(":", ""), "Monkey ")
    items        = [int(item) for item in all_after(lines[i + 1], "items: ").split(", ")]
    op_tokens    = lines[i + 2].split()
    operator_    = operator.mul if op_tokens[4] == "*" else operator.add
    op_value     = int(op_tokens[5]) if op_tokens[5] != "old" else "old"
    divisible_by = int(all_after(lines[i + 3], "divisible by "))
    true_throw   = int(all_after(lines[i + 4], "monkey "))
    false_throw  = int(all_after(lines[i + 5], "monkey "))
    if op_value == "old":
        operation = partial(pow, exp=2)
    else:
        operation = partial(operator_, op_value)
    return Monkeh(items, operation, divisible_by, true_throw, false_throw)

def monkeh_compute(lines: list[str], iterations: int, part2=False) -> int:
    monkey_start_line_indexes = [i for i, line in enumerate(lines) if line.startswith("Monkey")]
    monkehs = [parse_monkeh(lines, i) for i in monkey_start_line_indexes]
    monkeh_modulo = prod(monkeh.divisible_by for monkeh in monkehs)
    monkeh_inspections = Counter()
    for rundi in range(iterations):
        for monkeh in monkehs:
            for item in monkeh.items:
                new = monkeh.operation(item)
                if part2:
                    # Stupid mafs monkehs no need to know
                    new %= monkeh_modulo
                else:
                    new //= 3
                if new % monkeh.divisible_by == 0:
                    monkehs[monkeh.true_throw].items.append(new)
                else:
                    monkehs[monkeh.false_throw].items.append(new)
                monkeh_inspections[monkeh] += 1
            monkeh.items.clear()
    return prod(value for item, value in monkeh_inspections.most_common(2))

with open("input.txt") as f:
    lines = f.read().splitlines()

print(monkeh_compute(lines, 20))
print(monkeh_compute(lines, 10000, part2=True))
