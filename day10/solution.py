from collections import namedtuple
import sys

Point = namedtuple("Point", ["x", "y"])

with open("day10/input.txt") as f:
    lines = f.read().splitlines()
    maze = [list(line) for line in lines]
    for y, line in enumerate(maze):
        if "S" in line:
            start = Point(line.index("S"), y)

sys.setrecursionlimit(25000)


def get_reachable(pos: Point) -> list[Point]:
    match maze[pos.y][pos.x]:
        case "S":
            return []
        case "|":
            return [Point(pos.x, pos.y - 1), Point(pos.x, pos.y + 1)]
        case "-":
            return [Point(pos.x - 1, pos.y), Point(pos.x + 1, pos.y)]
        case "L":  # north and east
            return [Point(pos.x, pos.y - 1), Point(pos.x + 1, pos.y)]
        case "J":  # north and west
            return [Point(pos.x, pos.y - 1), Point(pos.x - 1, pos.y)]
        case "7":  # south and west
            return [Point(pos.x, pos.y + 1), Point(pos.x - 1, pos.y)]
        case "F":  # south and east
            return [Point(pos.x, pos.y + 1), Point(pos.x + 1, pos.y)]
        case _:
            return []


def follow(steps):
    curr = steps[-1]

    reachable = get_reachable(curr)
    reachable = [pos for pos in reachable if pos not in steps]

    if len(reachable) == 1:
        steps.append(reachable[0])
        return follow(steps)

    return steps


def get_adjacent(pos: Point):
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_pos = Point(pos.x + i, pos.y + j)
            yield new_pos


longest_path = []
for pos in get_adjacent(start):
    path = follow([start, pos])
    if len(path) > len(longest_path):
        longest_path = path

print(f"Steps to furthest point: {len(longest_path) // 2}")


nodes = set(longest_path)
enclosed = 0
for y in range(len(maze)):
    inside = False
    for x in range(len(maze[0])):
        pos = Point(x, y)

        if maze[pos.y][pos.x] in "|JLS" and pos in nodes:
            inside = not inside

        if inside and pos not in nodes:
            enclosed += 1

print(f"Enclosed area: {enclosed}")
