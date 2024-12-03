from collections import namedtuple
import re
from itertools import combinations
from decimal import Decimal as D

Stone = namedtuple("Stone", ["px", "py", "pz", "vx", "vy", "vz"])
Point = namedtuple("Point", ["x", "y"])

origin = Point(D("0.0"), D("0.0"))

with open("2023/day24/input.txt") as f:
    lines = f.read().splitlines()
    stones = []
    for line in lines:
        stones.append(Stone(*map(D, re.findall(r"-?\d+", line))))


def determine_t(stone: Stone, inter: Point) -> D:
    if stone.vx != 0:
        return (inter.x - stone.px) / stone.vx
    return (inter.y - stone.py) / stone.vy


def check_hailstones(fst: Stone, snd: Stone) -> Point | None:
    """Calculate the intersection of two stones' paths."""
    try:
        fst_t = determine_t(fst, origin)
        snd_t = determine_t(snd, origin)
    except:
        return None

    c = fst.py + fst.vy * fst_t
    a = fst.vy / fst.vx

    d = snd.py + snd.vy * snd_t
    b = snd.vy / snd.vx

    if a == b:  # Lines are parallel
        return None

    x = (d - c) / (a - b)
    y = a * x + c

    return Point(x.quantize(D("1.")), y.quantize(D("1.")))


def not_in_past(stone: Stone, x: D) -> bool:
    """Check if a point is in the past of a stone."""
    return (x - stone.px) / stone.vx > 0


def inside_area(x: D, y: D, area: tuple[float, float]) -> bool:
    """Check if a point is inside a square area."""
    return area[0] <= x <= area[1] and area[0] <= y <= area[1]


# area = (7, 27)
area = (200000000000000, 400000000000000)


total = 0
for fst, snd in combinations(stones, 2):
    res = check_hailstones(fst, snd)
    if res is None:
        continue
    x, y = res
    if inside_area(x, y, area) and not_in_past(fst, x) and not_in_past(snd, x):
        total += 1

print(f"Num intersecting paths: {total}")


def update_velocity(stone: Stone, vx: int, vy: int) -> Stone:
    """Update the velocity of a stone."""
    return Stone(stone.px, stone.py, stone.pz, stone.vx - vx, stone.vy - vy, stone.vz)


def determine_z_vel(fst: Stone, snd: Stone, inter) -> D | None:
    try:
        fst_t = determine_t(fst, inter)
        snd_t = determine_t(snd, inter)
    except:
        return None

    fst_dist = fst.pz + fst.vz * fst_t
    snd_dist = snd.pz + snd.vz * snd_t

    return (fst_dist - snd_dist) / (fst_t - snd_t)


for x_vel in range(-250, 250):
    for y_vel in range(-250, 250):
        print(f"Checking {x_vel}, {y_vel}")

        # Pretend our stone is standing still
        # all stones should intercept our stone at the same point in space
        fst = update_velocity(stones[0], x_vel, y_vel)
        intersection = check_hailstones(fst, update_velocity(stones[1], x_vel, y_vel))

        if intersection is None:
            continue

        passes = True
        for other in stones[2:]:
            snd = update_velocity(other, x_vel, y_vel)
            res = check_hailstones(fst, snd)

            if res and not_in_past(fst, res[0]) and not_in_past(snd, res[0]):
                if intersection == res:
                    continue

            passes = False
            break

        # Calculate z coordinate of the intercept
        if passes:
            print(f"intersection found at {intersection}")

            t = determine_t(fst, intersection)
            vz = determine_z_vel(fst, update_velocity(stones[1], x_vel, y_vel), intersection)

            z = fst.pz + t * (fst.vz - vz)
            print(f"Found at {intersection[0]}, {intersection[1]}, {z}")
            print(intersection[0] + intersection[1] + z)
            exit(0)
