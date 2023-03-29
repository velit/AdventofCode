from common.coord import Coord


def grouper(iterable, n):
    args = [iter(iterable)] * n
    return zip(*args, strict=True)

def manhattan_distance(a: Coord, b: Coord) -> int:
    return abs(a.y - b.y) + abs(a.x - b.x)

def all_after(content: str, separator: str) -> str:
    """Return the content after the given separator."""
    return content.partition(separator)[2]

def token_after(content: str, separator: str) -> str:
    """Return the next token after the given separator."""
    return content.partition(separator)[2].split()[0]
