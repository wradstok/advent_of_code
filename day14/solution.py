with open("day14/input.txt") as f:
    lines = f.read().splitlines()
    lines = [list(line) for line in lines]
    height = len(lines)
    width = len(lines[0])

rock_positions = []
unmovable = set()

for y in range(height):
    for x in range(width):
        if lines[y][x] == "O":
            rock_positions.append((x, y))
        if lines[y][x] == "#":
            unmovable.add((x, y))


def get_load(rocks):
    return sum([height - y for _, y in rocks])


def print_rocks(rocks, unmovable):
    for y in range(height):
        line = []
        for x in range(width):
            if (x, y) in unmovable:
                line.append("#")
            elif (x, y) in rocks:
                line.append("O")
            else:
                line.append(".")
        print("".join(line))


def shift_north(rocks):
    new_positions = []
    for x, y in rocks:
        end = 0
        for s in range(y, -1, -1):
            if (x, s) in unmovable:
                end = s + 1
                break

        path = [(x, s) for s in range(end, y)]
        rocks_between = sum([1 for (a, b) in path if (a, b) in rocks])

        pos = end + rocks_between
        new_positions.append((x, pos))

    return new_positions


def shift_south(rocks):
    new_positions = []
    for x, y in rocks:
        end = height - 1
        for s in range(y, height):
            if (x, s) in unmovable:
                end = s - 1
                break

        path = [(x, s) for s in range(y + 1, end + 1)]
        rocks_between = sum([1 for (a, b) in path if (a, b) in rocks])

        pos = end - rocks_between
        new_positions.append((x, pos))

    return new_positions


def shift_west(rocks):
    new_positions = []
    for x, y in rocks:
        end = 0
        for s in range(x, -1, -1):
            if (s, y) in unmovable:
                end = s + 1
                break

        path = [(s, y) for s in range(end, x)]
        rocks_between = sum([1 for (a, b) in path if (a, b) in rocks])

        pos = end + rocks_between
        new_positions.append((pos, y))

    return new_positions


def shift_east(rocks):
    new_positions = []
    for x, y in rocks:
        end = width - 1
        for s in range(x, width):
            if (s, y) in unmovable:
                end = s - 1
                break

        path = [(s, y) for s in range(x + 1, end + 1)]
        rocks_between = sum([1 for (a, b) in path if (a, b) in rocks])

        pos = end - rocks_between
        new_positions.append((pos, y))

    return new_positions


# Part 1
# rock_positions = shift_north(rock_positions)
# print(get_load(rock_positions))


# Part 2
def shift_all(rocks):
    rocks = shift_north(rocks)
    rocks = shift_west(rocks)
    rocks = shift_south(rocks)
    rocks = shift_east(rocks)

    return rocks


cycles = 1_000_000_000
hashes = {}
i = 0
cycled = False
while True:
    if i == cycles:
        break

    h = hash(tuple(rock_positions))

    # We reached a cycle, we can fast forward
    if h in hashes and not cycled:
        period = i - hashes[h]
        print(f"Cycle found of size {period} at {i}")

        remaining = cycles - i
        i += remaining // period * period
        cycled = True
        continue

    hashes[h] = i
    rock_positions = shift_all(rock_positions)

    i += 1


print(get_load(rock_positions))
