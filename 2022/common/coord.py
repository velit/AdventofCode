from __future__ import annotations

from dataclasses import dataclass


@dataclass(order=True, frozen=True)
class Coord:
    y: int = 0
    x: int = 0

    def __add__(self, other: Coord) -> Coord:
        return Coord(self.y + other.y, self.x + other.x)

    def __sub__(self, other: Coord) -> Coord:
        return Coord(self.y - other.y, self.x - other.x)

    def __len__(self):
        return 2

    def __getitem__(self, key):
        if key == 0:
            return self.y
        if key == 1:
            return self.x
        raise IndexError(f"Invalid {key=}")

@dataclass(order=True, frozen=True)
class Position:
    x: int = 0
    y: int = 0
    z: int = 0

    def __add__(self, other: Position) -> Position:
        return Position(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Position) -> Position:
        return Position(self.x - other.x, self.y - other.y, self.z - other.z)

    def __len__(self):
        return 3

    def __getitem__(self, key):
        if key == 0:
            return self.x
        if key == 1:
            return self.y
        if key == 2:
            return self.z
        raise IndexError(f"Invalid {key=}")
