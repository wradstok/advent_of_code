from collections import namedtuple, defaultdict, deque

with open("day23/input.txt") as f:
    grid = f.read().splitlines()
    height, width = len(grid), len(grid[0])

Point = namedtuple("Point", ["x", "y"])


def get_adjacent(pos: Point) -> list[Point]:
    match grid[pos.y][pos.x]:
        # Uncomment to solve p1
        # case "^":
        #     options = [Point(pos.x, pos.y - 1)]
        # case "v":
        #     options = [Point(pos.x, pos.y + 1)]
        # case "<":
        #     options = [Point(pos.x - 1, pos.y)]
        # case ">":
        #     options = [Point(pos.x + 1, pos.y)]
        case _:
            options = [
                Point(pos.x + 1, pos.y),
                Point(pos.x - 1, pos.y),
                Point(pos.x, pos.y + 1),
                Point(pos.x, pos.y - 1),
            ]

    valid = []
    for option in options:
        if 0 <= option.x < width and 0 <= option.y < height:
            if grid[option.y][option.x] != "#":
                valid.append(option)
    return valid


def follow(curr: Point, prev: Point, size: int) -> tuple[Point, int]:
    options = get_adjacent(curr)
    options = [o for o in options if o != prev]

    if len(options) == 0:
        return curr, size

    if len(options) > 1:
        return curr, size

    return follow(options[0], curr, size + 1)


def get_neighbours(curr: Point) -> dict[Point, int]:
    direct_neighbours = get_adjacent(curr)

    options = [follow(neighbour, curr, 1) for neighbour in direct_neighbours]
    options = {node: size for (node, size) in options if node != curr}

    return options


start = Point(1, 0)
end = Point(width - 2, height - 1)

nodes: dict[Point, dict[Point, int]] = defaultdict(dict)
nodequeue: list[Point] = [start]

# Convert to graph
while nodequeue:
    prev = nodequeue.pop()
    neighbours = get_neighbours(prev)
    nodes[prev] = neighbours

    unseen = [node for node in neighbours if node not in nodes]
    nodequeue.extend(unseen)


# Generate all simple paths
queue: deque[tuple[Point, int, set[Point]]] = deque([(start, 0, set())])
max_size = 0

while queue:
    curr, size, seen = queue.pop()
    if curr == end:
        max_size = max(max_size, size)
        continue

    for neighbour in nodes[curr]:
        if neighbour not in seen:
            copy = seen.copy()
            copy.add(neighbour)
            queue.append((neighbour, size + nodes[curr][neighbour], copy))


print(max_size)
