from collections import namedtuple

with open("2024/day06/input.txt") as f:
    data = f.readlines()

Point = namedtuple("Point", ["x", "y"])

orig_guard = Point(0, 0)
obstacles_by_y: dict[int, set[Point]] = {}
obstacles_by_x: dict[int, set[Point]] = {}

for y, line in enumerate(data):
    obstacles = set([Point(x, y) for x, item in enumerate(line) if item == "#"])
    obstacles_by_y[y] = obstacles

    for o in obstacles:
        obstacles_by_x[o.x] = obstacles_by_x.get(o.x, set()) | {o}

    if "^" in line:
        orig_guard = Point(line.index("^"), y)


possible_blockers = []
guard_dir = "up"

for pos_y in range(len(data)):
    for pos_x in range(len(data[0])):
        guard = orig_guard
        guard_dir = "up"

        seen_positions: set[tuple[Point, str]] = {(orig_guard, guard_dir)}

        new_obstacle = Point(pos_x, pos_y)
        if new_obstacle == guard or new_obstacle in obstacles_by_x.get(new_obstacle.x, set()):
            continue

        obstacles_by_x[new_obstacle.x] = obstacles_by_x.get(new_obstacle.x, set()) | {new_obstacle}
        obstacles_by_y[new_obstacle.y] = obstacles_by_y.get(new_obstacle.y, set()) | {new_obstacle}

        while True:
            match guard_dir:
                case "up":
                    possible_hits = [p for p in obstacles_by_x[guard.x] if p.y < guard.y]
                    if possible_hits:
                        hit = max(possible_hits, key=lambda p: p.y)
                        guard = Point(guard.x, hit.y + 1)

                        guard_dir = "right"
                        if (guard, guard_dir) in seen_positions:
                            possible_blockers.append(new_obstacle)
                            break
                        seen_positions.add((guard, guard_dir))

                    else:
                        break
                case "right":
                    possible_hits = [p for p in obstacles_by_y[guard.y] if p.x > guard.x]
                    if possible_hits:
                        hit = min(possible_hits, key=lambda p: p.x)
                        guard = Point(hit.x - 1, guard.y)

                        guard_dir = "down"
                        if (guard, guard_dir) in seen_positions:
                            possible_blockers.append(new_obstacle)
                            break
                        seen_positions.add((guard, guard_dir))
                    else:
                        break
                case "down":
                    possible_hits = [p for p in obstacles_by_x[guard.x] if p.y > guard.y]
                    if possible_hits:
                        hit = min(possible_hits, key=lambda p: p.y)
                        guard = Point(guard.x, hit.y - 1)

                        guard_dir = "left"
                        if (guard, guard_dir) in seen_positions:
                            possible_blockers.append(new_obstacle)
                            break
                        seen_positions.add((guard, guard_dir))

                    else:
                        break
                case "left":
                    possible_hits = [p for p in obstacles_by_y[guard.y] if p.x < guard.x]
                    if possible_hits:
                        hit = max(possible_hits, key=lambda p: p.x)
                        guard = Point(hit.x + 1, guard.y)

                        guard_dir = "up"
                        if (guard, guard_dir) in seen_positions:
                            possible_blockers.append(new_obstacle)
                            break
                        seen_positions.add((guard, guard_dir))
                    else:
                        break

        obstacles_by_x[new_obstacle.x].remove(new_obstacle)
        obstacles_by_y[new_obstacle.y].remove(new_obstacle)

print(len(possible_blockers))
