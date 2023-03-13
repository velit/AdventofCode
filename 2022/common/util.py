from common.coord import Coord


def grouper(iterable, n):
    args = [iter(iterable)] * n
    return zip(*args, strict=True)

def manhattan_distance(a: Coord, b: Coord) -> int:
    return abs(a.y - b.y) + abs(a.x - b.x)
