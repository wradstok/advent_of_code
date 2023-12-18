from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

with open("day18/input.txt") as f:
    lines = f.read().splitlines()
    lines = [line.split() for line in lines]
    fixed = []
    convert = {"0": "R", "1": "D", "2": "L", "3": "U"}
    for line in lines:
        line = line[2].lstrip("(#").rstrip(")")
        dir, dist = line[-1], line[:-1]
        fixed.append((convert[dir], int(dist, base=16)))


polygon: list[Point] = [Point(0, 0)]
for dir, dist in fixed:
    prev = polygon[-1]
    match dir:
        case "U":
            polygon.append(Point(prev.x, prev.y - int(dist)))
        case "D":
            polygon.append(Point(prev.x, prev.y + int(dist)))
        case "L":
            polygon.append(Point(prev.x - int(dist), prev.y))
        case "R":
            polygon.append(Point(prev.x + int(dist), prev.y))


polygon.reverse()

# Inside area
area = 0
for fst, snd, trd in zip(polygon, polygon[1:], polygon[2:]):
    area += snd.x * (fst.y - trd.y)

area = area // 2

# Circumference
circumference = 0
for fst, snd in zip(polygon, polygon[1:]):
    circumference += abs(fst.x - snd.x) + abs(fst.y - snd.y)

total = area + circumference // 2 + 1

# I'm not entirely sure why this works.. but I found the realisation by playing with the numbers
# after implementing the first part using floodfill
