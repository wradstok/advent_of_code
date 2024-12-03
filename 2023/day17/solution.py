import heapq
from collections import namedtuple, defaultdict

with open("2023/day17/input.txt") as f:
    lines = f.read().splitlines()
    heat = []
    for line in lines:
        heat.append(list(map(int, line)))


MovePoint = namedtuple("MovePoint", ["x", "y", "dir", "steps"])


def get_adjacent(point: MovePoint) -> list[MovePoint]:
    options: list[MovePoint] = []

    # Generate all reachable tiles
    reverse = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
    for dir in ["UP", "DOWN", "LEFT", "RIGHT"]:
        if dir == reverse[point.dir]:
            continue

        steps = point.steps + 1 if dir == point.dir else 1
        match dir:
            case "UP":
                options.append(MovePoint(point.x, point.y - 1, dir, steps))
            case "DOWN":
                options.append(MovePoint(point.x, point.y + 1, dir, steps))
            case "LEFT":
                options.append(MovePoint(point.x - 1, point.y, dir, steps))
            case "RIGHT":
                options.append(MovePoint(point.x + 1, point.y, dir, steps))

    # Filter out tiles which are outside the map
    real_options: list[MovePoint] = []
    for option in options:
        if 0 <= option.x < len(heat[0]) and 0 <= option.y < len(heat):
            if option.steps < 4:
                real_options.append(option)

    return real_options


def get_adjacent_ultra(point: MovePoint) -> list[MovePoint]:
    options: list[MovePoint] = []

    # Generate all reachable tiles
    reverse = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
    for dir in ["UP", "DOWN", "LEFT", "RIGHT"]:
        if dir == reverse[point.dir]:
            continue

        steps = point.steps + 1 if dir == point.dir else 1
        match dir:
            case "UP":
                options.append(MovePoint(point.x, point.y - 1, dir, steps))
            case "DOWN":
                options.append(MovePoint(point.x, point.y + 1, dir, steps))
            case "LEFT":
                options.append(MovePoint(point.x - 1, point.y, dir, steps))
            case "RIGHT":
                options.append(MovePoint(point.x + 1, point.y, dir, steps))

    # Filter out tiles which are outside the map
    real_options: list[MovePoint] = []
    for option in options:
        if 0 <= option.x < len(heat[0]) and 0 <= option.y < len(heat):
            # If continuing in same direction, only allow max 10 steps
            if option.dir == point.dir:
                if option.steps <= 10:
                    real_options.append(option)
            # Changing directions is only possible if minimum 4 steps done
            else:
                if point.steps >= 4:
                    real_options.append(option)

    return real_options


dist = defaultdict(lambda: 99999999)
heap: list[tuple[int, MovePoint]] = []

starts = [MovePoint(0, 4, "DOWN", 4), MovePoint(4, 0, "RIGHT", 4)]

dist[MovePoint(0, 4, "DOWN", 4)] = sum(heat[0][1:5])
dist[MovePoint(4, 0, "RIGHT", 4)] = sum(heat[0][1:5])
for start in starts:
    heapq.heappush(heap, (dist[start], start))


found = False
while len(heap) > 0 and not found:
    _, point = heapq.heappop(heap)

    for adj in get_adjacent_ultra(point):
        alt = dist[point] + heat[adj.y][adj.x]

        if adj.x == len(heat[0]) - 1 and adj.y == len(heat) - 1:
            print(alt)
            found = True
            break

        if alt < dist[adj]:
            dist[adj] = alt
            heapq.heappush(heap, (alt, adj))
