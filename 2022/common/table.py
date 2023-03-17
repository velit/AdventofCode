from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, InitVar, field
from itertools import zip_longest
from random import randrange
from typing import TypeVar, Generic, Iterator

from common.coord import Coord
from common.dimensions import Dimensions, DimensionsMixin

T = TypeVar('T')

@dataclass
class Table(Generic[T], DimensionsMixin):
    """
    Mutable non-dynamic array with two-dimensional get- and setitem methods.

    Iterating over the whole array gives all items directly by iterating the columns tighter i.e. 'line-by-line'.

    Underlying implementation is a one-dimensional dynamic list.
    """

    dimensions:  Dimensions
    init_values: InitVar[Iterable[T]] = ()
    fill_value:  InitVar[T | None]    = None
    _impl:       list[T]              = field(init=False, repr=False)

    def __post_init__(self, init_values: Iterable[T], fill_value: T | None) -> None:
        if fill_value is not None:
            self._impl: list[T] = list(value for _, value in zip_longest(range(self.dimensions.area), init_values,
                                                                         fillvalue=fill_value))
            if len(self) > self.dimensions.area:
                raise ValueError(f"Given {len(self)=} exceed {self.dimensions.area=}.")
        else:
            self._impl = list(init_values)
            if len(self) != self.dimensions.area:
                raise ValueError(f"Given {len(self)=} differs from {self.dimensions.area=} with no fillvalue")

    def __getitem__(self, coord: Coord | tuple[int, int]) -> T:
        return self._impl[self.get_index(coord)]

    def __setitem__(self, coord: Coord | tuple[int, int], value: T) -> None:
        self._impl[self.get_index(coord)] = value

    def __len__(self) -> int:
        return len(self._impl)

    def __contains__(self, value: T) -> bool:
        return value in self._impl

    def __iter__(self) -> Iterator[T]:
        return iter(self._impl)

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Table):
            return self.dimensions == o.dimensions and self._impl == o._impl
        return False

    def __str__(self):
        max_size = max(len(str(item)) for item in self._impl)
        if max_size > 1:
            max_size += 1
        return "\n".join("".join(f"{col: <{max_size}}" for col in row) for row in self.row_by_row())

    def str_row_inverted(self):
        max_size = max(len(str(item)) for item in self._impl)
        if max_size > 1:
            max_size += 1
        return "\n".join("".join(f"{col: <{max_size}}" for col in row) for row in self.row_by_row_reversed())

    def increase_first_dimension(self, amount: int, fill_value: T | None = None) -> None:
        self._impl.extend([fill_value] * self.cols * amount)
        self.dimensions = Dimensions(self.rows + amount, self.cols)

    def get_coord(self, index: int) -> Coord:
        return self.dimensions.get_coord(index)

    def get_index(self, coord: Coord | tuple[int, int]) -> int:
        return self.dimensions.get_index(coord)

    def is_legal(self, coord: Coord | tuple[int, int]) -> bool:
        y, x = coord
        return (0 <= y < self.rows) and (0 <= x < self.cols)

    def fill(self, fill_value: T) -> None:
        for i in range(self.dimensions.area):
            self[self.get_coord(i)] = fill_value

    def enumerate(self) -> Iterable[tuple[Coord, T]]:
        for i, item in enumerate(self):
            yield self.get_coord(i), item

    def row_by_row(self) -> Iterable[Iterable[T]]:
        for row in range(self.rows):
            row_start = row * self.cols
            row_limit = row_start + self.cols
            yield self._impl[row_start:row_limit]

    def row_by_row_reversed(self) -> Iterable[Iterable[T]]:
        for row in reversed(range(self.rows)):
            row_start = row * self.cols
            row_limit = row_start + self.cols
            yield self._impl[row_start:row_limit]

    def col_by_col(self) -> Iterable[Iterable[T]]:
        for col in range(self.cols):
            yield self._impl[col::self.rows]

    def coord_iter(self) -> Iterable[Coord]:
        for i, item in enumerate(self):
            yield self.get_coord(i)

    def random_coord(self) -> Coord:
        return Coord(randrange(self.rows), randrange(self.cols))
