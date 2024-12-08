from collections import defaultdict, namedtuple

Point = namedtuple("Point", ["x", "y"])

with open("2024/day08/input.txt", "r") as f:
    data = f.read().splitlines()

    antennas = defaultdict(list)
    for y, line in enumerate(data):
        for x, item in enumerate(line):
            if item == ".":
                continue
            antennas[item].append(Point(x, y))

antinodes: set[Point] = set()
for kind, positions in antennas.items():
    for i, antenna in enumerate(positions):
        for j, other in enumerate(positions[i + 1 :]):
            diff = Point(antenna.x - other.x, antenna.y - other.y)

            p1 = Point(antenna.x + diff.x, antenna.y + diff.y)
            p2 = Point(other.x - diff.x, other.y - diff.y)
            antinodes |= {p1, p2}

valid_count = 0
for node in antinodes:
    if 0 <= node.x < len(data[0]) and 0 <= node.y < len(data):
        valid_count += 1

print(valid_count)


antinodes: set[Point] = set()

for kind, positions in antennas.items():
    for i, antenna in enumerate(positions):
        for j, other in enumerate(positions[i + 1 :]):
            diff = Point(antenna.x - other.x, antenna.y - other.y)

            i = 0
            while True:
                p1 = Point(antenna.x + i * diff.x, antenna.y + i * diff.y)
                if not (0 <= p1.x < len(data[0]) and 0 <= p1.y < len(data)):
                    break

                antinodes.add(p1)
                i += 1

            i = 0
            while True:
                p2 = Point(other.x - i * diff.x, other.y - i * diff.y)
                if not (0 <= p2.x < len(data[0]) and 0 <= p2.y < len(data)):
                    break

                antinodes.add(p2)
                i += 1


print(len(antinodes))
