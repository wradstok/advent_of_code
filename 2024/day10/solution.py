from collections import namedtuple

with open("2024/day10/input.txt") as f:
    data = f.read().splitlines()

heightmap = []
for i, line in enumerate(data):
    heightmap.append(list(map(int, line)))

Point = namedtuple("Point", ["x", "y"])

starting_positions = []
for y, line in enumerate(heightmap):
    for x, height in enumerate(line):
        if height == 0:
            starting_positions.append(Point(x, y))


def get_adjacent(point):
    options = [
        Point(point.x + 1, point.y),
        Point(point.x - 1, point.y),
        Point(point.x, point.y + 1),
        Point(point.x, point.y - 1),
    ]

    valid_options = []
    for option in options:
        if (
            0 <= option.y < len(heightmap)
            and 0 <= option.x < len(heightmap[0])
            and heightmap[option.y][option.x] == heightmap[point.y][point.x] + 1
        ):
            valid_options.append(option)

    return valid_options


num_found = 0
for pos in starting_positions:
    reachable = get_adjacent(pos)
    # seen = set()
    while True:
        if not reachable:
            break

        item = reachable.pop()

        if heightmap[item.y][item.x] == 9:
            # if item not in seen:
            #     seen.add(item)
            num_found += 1
            continue

        next_reachable = get_adjacent(item)
        reachable.extend(next_reachable)


print(num_found)
