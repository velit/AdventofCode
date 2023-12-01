#!/usr/bin/env python3

import re

def main() -> None:
    with open("input") as f:
        lines = f.read().splitlines()

    print(sum(int(number_line[0] + number_line[-1]) for number_line in strip_non_numbers(lines)))
    print(sum(int(number_line[0] + number_line[-1]) for number_line in convert_numbers(lines)))

def strip_non_numbers(lines: list[str]) -> list[str]:
    return [re.sub("[^0-9]", "", line) for line in lines]

def convert_numbers(lines: list[str]) -> list[str]:
    return [convert_line(line) for line in lines]

def convert_line(line: str) -> str:
    new_line = []
    for i in range(len(line)):
        if line[i].isdigit():
            new_line.append(line[i])
        if line[i:].startswith("one"):   new_line.append("1")
        if line[i:].startswith("two"):   new_line.append("2")
        if line[i:].startswith("three"): new_line.append("3")
        if line[i:].startswith("four"):  new_line.append("4")
        if line[i:].startswith("five"):  new_line.append("5")
        if line[i:].startswith("six"):   new_line.append("6")
        if line[i:].startswith("seven"): new_line.append("7")
        if line[i:].startswith("eight"): new_line.append("8")
        if line[i:].startswith("nine"):  new_line.append("9")
        if line[i:].startswith("zero"):  new_line.append("0")
    return "".join(new_line)

if __name__ == "__main__":
    main()
