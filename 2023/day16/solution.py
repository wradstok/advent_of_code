from enum import Enum
from collections import namedtuple

with open("2023/day16/input.txt") as f:
    lines = f.read().splitlines()


Point = namedtuple("Point", ["x", "y"])


class Dir(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


Beam = namedtuple("Beam", ["pos", "dir"])


def move_beam(beam: Beam) -> list[Beam]:
    match beam.dir:
        case Dir.UP:
            next_pos = Point(beam.pos.x, beam.pos.y - 1)
            if next_pos.y < 0:
                return []

            match lines[next_pos.y][next_pos.x]:
                case ".":
                    return [Beam(next_pos, Dir.UP)]
                case "/":
                    return [Beam(next_pos, Dir.RIGHT)]
                case "\\":
                    return [Beam(next_pos, Dir.LEFT)]
                case "|":
                    return [Beam(next_pos, Dir.UP)]
                case "-":
                    return [Beam(next_pos, Dir.LEFT), Beam(next_pos, Dir.RIGHT)]
        case Dir.RIGHT:
            next_pos = Point(beam.pos.x + 1, beam.pos.y)
            if next_pos.x >= len(lines[0]):
                return []

            match lines[next_pos.y][next_pos.x]:
                case ".":
                    return [Beam(next_pos, Dir.RIGHT)]
                case "/":
                    return [Beam(next_pos, Dir.UP)]
                case "\\":
                    return [Beam(next_pos, Dir.DOWN)]
                case "|":
                    return [Beam(next_pos, Dir.UP), Beam(next_pos, Dir.DOWN)]
                case "-":
                    return [Beam(next_pos, Dir.RIGHT)]
        case Dir.DOWN:
            next_pos = Point(beam.pos.x, beam.pos.y + 1)
            if next_pos.y >= len(lines):
                return []

            match lines[next_pos.y][next_pos.x]:
                case ".":
                    return [Beam(next_pos, Dir.DOWN)]
                case "/":
                    return [Beam(next_pos, Dir.LEFT)]
                case "\\":
                    return [Beam(next_pos, Dir.RIGHT)]
                case "|":
                    return [Beam(next_pos, Dir.DOWN)]
                case "-":
                    return [Beam(next_pos, Dir.LEFT), Beam(next_pos, Dir.RIGHT)]
        case Dir.LEFT:
            next_pos = Point(beam.pos.x - 1, beam.pos.y)
            if next_pos.x < 0:
                return []

            match lines[next_pos.y][next_pos.x]:
                case ".":
                    return [Beam(next_pos, Dir.LEFT)]
                case "/":
                    return [Beam(next_pos, Dir.DOWN)]
                case "\\":
                    return [Beam(next_pos, Dir.UP)]
                case "|":
                    return [Beam(next_pos, Dir.UP), Beam(next_pos, Dir.DOWN)]
                case "-":
                    return [Beam(next_pos, Dir.LEFT)]

    raise ValueError()


def trace_beam(beam) -> int:
    seen = set([beam])
    beams = [beam]

    while True:
        next_round = []
        for beam in beams:
            next_round.extend(move_beam(beam))

        next_round = [beam for beam in next_round if beam not in seen]

        if len(next_round) == 0:
            break

        seen.update(next_round)
        beams = next_round

    energized = set((item.pos for item in seen))
    return len(energized)


# Part 1
print(trace_beam(Beam(Point(0, 0), Dir.RIGHT)))


# Part 2
start_options = []
for x in range(0, len(lines[0])):
    start_options.append(Beam(Point(x, 0), Dir.DOWN))
    start_options.append(Beam(Point(x, len(lines) - 1), Dir.UP))

for y in range(0, len(lines)):
    start_options.append(Beam(Point(0, y), Dir.RIGHT))
    start_options.append(Beam(Point(len(lines[0]) - 1, y), Dir.LEFT))

highest = 0
for start in start_options:
    highest = max(highest, trace_beam(start))
print(highest)
