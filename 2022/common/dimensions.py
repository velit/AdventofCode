from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from common.coord import Coord


@dataclass(order=True, frozen=True)
class Dimensions:
    rows: int
    cols: int

    def __add__(self, other: Dimensions) -> Dimensions:
        return Dimensions(self.rows + other.rows, self.cols + other.cols)

    def __len__(self):
        return 2

    def __getitem__(self, key):
        if key == 0:
            return self.rows
        if key == 1:
            return self.cols
        raise IndexError(f"Invalid {key=}")

    @property
    def area(self) -> int:
        return self.rows * self.cols

    @property
    def min(self) -> int:
        return min(self.rows, self.cols)

    def get_index(self, coord: Coord | tuple[int, int]) -> int:
        row, col = coord
        if row < self.rows and col < self.cols:
            return row * self.cols + col
        raise IndexError(f"{coord=} out of range for {self=}")

    def get_coord(self, index: int) -> Coord:
        return Coord(index // self.cols, index % self.cols)


class HasDimensions(Protocol):

    @property
    def dimensions(self) -> Dimensions:
        raise NotImplementedError


class DimensionsMixin:

    @property
    def rows(self: HasDimensions) -> int:
        return self.dimensions.rows

    @property
    def cols(self: HasDimensions) -> int:
        return self.dimensions.cols
