#!/usr/bin/env python3
from collections import deque


def main(part2=False) -> None:
    n = 1
    mult = 1
    if part2:
        n = 10
        mult = 811589153
    with open("input.txt") as f:
        lines = [(i, int(number) * mult) for i, number in enumerate(f.read().splitlines())]
        value = dict(lines)
        deq: deque[tuple[int, int] | int] = deque(lines)

    for _ in range(n):
        for number in range(len(deq)):
            index = deq.index((number, value[number]))
            deq.rotate(-index)
            i, val = deq.popleft()
            deq.rotate(-val)
            deq.appendleft((i, val))

    zero_i = deq.index((4449, 0))

    def zero_offset(i: int) -> int:
        return deq[(zero_i + i) % len(deq)][1]

    print(zero_offset(1000) + zero_offset(2000) + zero_offset(3000))

if __name__ == "__main__":
    main()
    main(part2=True)
