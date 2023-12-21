from collections import namedtuple
from functools import cache

with open("day21/input.txt") as f:
    lines = f.read().splitlines()

Point = namedtuple("Point", ["x", "y"])


@cache
def get_adjacent(pos: Point):
    adjacent = [
        Point(pos.x - 1, pos.y),
        Point(pos.x + 1, pos.y),
        Point(pos.x, pos.y - 1),
        Point(pos.x, pos.y + 1),
    ]

    valid = []
    for adj in adjacent:
        fake_x = adj.x % len(lines[0])
        fake_y = adj.y % len(lines)
        if lines[fake_y][fake_x] != "#":
            valid.append(adj)
    return valid


for y, line in enumerate(lines):
    if "S" in line:
        start = Point(y, line.index("S"))
        break

width, height = len(lines[0]), len(lines)


starts = {
    height // 2 + height * 0: 0,
    height // 2 + height * 1: 0,
    height // 2 + height * 2: 0,
}

# I don't fully deserve the second star.. Couldn't do it without help :(
positions = set([start])
for iteration in range(height // 2 + height * 2):
    if iteration in starts:
        starts[iteration] = len(positions)

    new_positions = set()
    for pos in positions:
        new_positions.update(get_adjacent(pos))
    positions = new_positions

starts[iteration] = len(positions)


def interpolate(n: int, a: int, b: int, c: int) -> int:
    fst = b - a
    snd = c - b
    return a + fst * n + ((n**2 - n) // 2) * (snd - fst)


steps = 26_501_365
res = interpolate(steps // len(lines), *starts.values())
print(res)
