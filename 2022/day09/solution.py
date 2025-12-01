import os
from collections import namedtuple

with open(os.getcwd() + "/day09/input.txt") as f:
    lines = f.read().splitlines()
    moves = [line.split() for line in lines] 

Point = namedtuple("Point", ["y", "x"])


def try_move_diagonally(head: Point, tail: Point) -> Point:
    # Same col or row?
    if head.y == tail.y or head.x == tail.x:
        return tail
    
    # Touching?
    if abs(head.y - tail.y) == 1 and abs(head.x - tail.x) == 1:
        return tail

    updown = -1 if head.y < tail.y else 1 
    leftright = -1 if head.x < tail.x else 1

    return Point(tail.y + updown, tail.x + leftright)


def move(point: Point, amount: int, direction: str):
    match direction:
        case "U":
            return Point(point.y - amount, point.x)
        case "D":
            return Point(point.y + amount, point.x)
        case "R":
            return Point(point.y, point.x + amount)
        case "L":
            return Point(point.y, point.x - amount)

# Part 1
visited = set()
head, tail = Point(0,0), Point(0,0)
for direction, amount in moves:
    for _ in range(int(amount)):
        head = move(head, 1, direction)
        if head == move(tail, 2, direction):
            tail = move(tail, 1, direction)
        else:
            tail = try_move_diagonally(head, tail)
        visited.add(tail)

print(len(visited))
# Part 2
visited = set()
rope = [Point(0,0) for _ in range(10)]
for direction, amount in moves:
    for _ in range(int(amount)):
        rope[0] = move(rope[0], 1, direction)
        for i in range(1, len(rope)):
            moved = False
            for l_dir in ["L", "R", "U", "D"]:
                if not moved and rope[i - 1] == move(rope[i], 2, l_dir):
                    rope[i] = move(rope[i], 1, l_dir)
                    moved = True
            if not moved:
                rope[i] = try_move_diagonally(rope[i-1], rope[i])
            if i == 9:
                visited.add(rope[i])


print(len(visited))


