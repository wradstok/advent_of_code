from itertools import combinations

with open("day11/input.txt") as f:
    lines = f.read().splitlines()
    universe = [list(line) for line in lines]

# Expand universe
v_insert = []
for y, line in enumerate(universe):
    if "#" not in line:
        v_insert.append(y)
h_insert = []
for y in range(len(universe[0])):
    line = [universe[j][y] for j in range(len(universe))]
    if "#" not in line:
        h_insert.append(y)

# Find pairs galaxies
galaxies = []
for y in range(len(universe)):
    for x in range(len(universe[0])):
        if universe[y][x] == "#":
            galaxies.append((y, x))

pairs = list(combinations(galaxies, 2))


def calc_dist(a, b):
    EXPANSION_SIZE = 1000000 - 1

    # Count number of occurrenes in v_insert between a and b or b and a
    start, end = min(a[0], b[0]), max(a[0], b[0])
    v_expansion = sum([1 for i in v_insert if start < i < end])

    start, end = min(a[1], b[1]), max(a[1], b[1])
    h_expansion = sum([1 for i in h_insert if start < i < end])

    if a[0] < b[0]:
        b = (b[0] + v_expansion * EXPANSION_SIZE, b[1])
    else:
        a = (a[0] + v_expansion * EXPANSION_SIZE, a[1])

    if a[1] < b[1]:
        b = (b[0], b[1] + h_expansion * EXPANSION_SIZE)
    else:
        a = (a[0], a[1] + h_expansion * EXPANSION_SIZE)

    return abs(a[0] - b[0]) + abs(a[1] - b[1])


print(sum(map(lambda x: calc_dist(x[0], x[1]), pairs)))
