from __future__ import annotations
from collections import namedtuple
from math import sqrt, prod
import heapq

Point = namedtuple("Point", ["x", "y", "z"])

with open("2025/day08/input.txt") as f:
    lines = f.read().splitlines()


boxes: list[Point] = []
for line in lines:
    boxes.append(Point(*map(int, line.split(","))))


def calc_dist(p1: Point, p2: Point) -> float:
    return sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2)


class Pair:
    def __init__(self, p1: Point, p2: Point, dist: float):
        self.p1 = p1
        self.p2 = p2
        self.dist = dist

    def __lt__(self, other: Pair) -> bool:
        return self.dist < other.dist


closest: list[Pair] = []
for i, b1 in enumerate(boxes):
    for b2 in boxes[i + 1 :]:
        dist = calc_dist(b1, b2)
        heapq.heappush(closest, Pair(b1, b2, dist))

# closest = heapq.nsmallest(1000, closest)


circuits: list[set[Point]] = [set([box]) for box in boxes]
while True:
    pair = heapq.heappop(closest)

    c1 = None
    c2 = None

    for circuit in circuits:
        if pair.p1 in circuit:
            c1 = circuit
        if pair.p2 in circuit:
            c2 = circuit

    if c1 is c2:
        continue

    circuits.remove(c1)
    circuits.remove(c2)

    new_circuit = c1.union(c2)
    circuits.append(new_circuit)

    if len(circuits) == 1:
        print(pair.p1.x * pair.p2.x)


# sizes = sorted(map(len, circuits), reverse=True)

# print(prod(sizes[:3]))
