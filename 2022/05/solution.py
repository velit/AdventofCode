#!/usr/bin/env python3
import re
from copy import deepcopy

with open("input.txt") as f:
    lines = f.read().splitlines()
    digits = re.compile(r"\d+")
    orders = [digits.findall(line) for line in lines[10:]]
    orders = [list(map(int, sections)) for sections in orders]
    print(orders)

crates1 = [
    list(),
    list("BSVZGPW"),
    list("JVBCZF"),
    list("VLMHNZDC"),
    list("LDMZPFJB"),
    list("VFCGJBQH"),
    list("GFQTSLB"),
    list("LGCZV"),
    list("NLG"),
    list("JFHC"),
]
crates2 = deepcopy(crates1)

for amount, source, target in orders:
    for i in range(amount):
        crates1[target].append(crates1[source].pop())

print("".join(crate[-1] for crate in crates1[1:]))

for amount, source, target in orders:
    popped = crates2[source][-amount:]
    del crates2[source][-amount:]
    crates2[target].extend(popped)

print("".join(crate[-1] for crate in crates2[1:]))
