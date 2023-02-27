from __future__ import annotations

from collections.abc import Iterator
# !/usr/bin/env python3
from dataclasses import dataclass, field
from typing import Self


@dataclass
class Node:
    name: str
    file_size: int
    is_folder: bool
    total_size: int = field(init=False, default=None)
    parent: Node = field(init=False, repr=False, default=None)
    children: dict[str, Node] = field(init=False, repr=False, default_factory=dict)

    def add_child(self, name: str, file_size: int, is_folder: bool):
        child = Node(name, file_size, is_folder)
        child.parent = self
        self.children[name] = child

    def __iter__(self) -> Iterator[Self]:
        yield self
        for child in self.children.values():
            yield from child

with open("input.txt") as f:
    lines = f.read().splitlines()

current = Node("", file_size=0, is_folder=True)
current.add_child("/", file_size=0, is_folder=True)
root = current.children["/"]

for command in lines:
    match command.split():
        case ["$", "cd", ".."]:
            current = current.parent
        case ["$", "cd", folder_name]:
            current = current.children[folder_name]
        case ["dir", folder_name]:
            current.add_child(folder_name, file_size=0, is_folder=True)
        case [file_size, file_name] if file_size.isdigit():
            current.add_child(file_name, int(file_size), is_folder=False)
        case ["$", "ls"]:
            pass
        case _:
            raise Exception("you suck")

def set_total_sizes(node) -> int:
    if node.total_size is not None:
        return node.total_size
    node.total_size = node.file_size + sum(map(set_total_sizes, node.children.values()))
    return node.total_size

set_total_sizes(root)
small_items = [item for item in root if item.total_size <= 100000 and item.is_folder]

# part 1
print(sum(item.total_size for item in small_items))

TOTAL_SPACE = 70000000
NEEDED_SPACE = 30000000
MIN_FREE = NEEDED_SPACE - (TOTAL_SPACE - root.total_size)

folders_big_enough = [item for item in root if item.total_size >= MIN_FREE and item.is_folder]
folders_big_enough.sort(key=lambda item: item.total_size)

print(folders_big_enough[0].total_size)
