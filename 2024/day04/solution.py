with open("2024/day04/input.txt") as f:
    data = f.read().splitlines()


count = 0
diffs = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "X":

            for i, (dy, dx) in enumerate(diffs):
                final_y, final_x = y + 3 * dy, x + 3 * dx
                if not (0 <= final_y < len(data) and 0 <= final_x < len(data[0])):
                    continue

                if (
                    data[y + dy][x + dx] == "M"
                    and data[y + 2 * dy][x + 2 * dx] == "A"
                    and data[y + 3 * dy][x + 3 * dx] == "S"
                ):
                    count += 1
print(count)


from collections import namedtuple

Point = namedtuple("Point", ["y", "x"])

mas: list[list[Point]] = []
diffs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "M":

            for i, (dy, dx) in enumerate(diffs):
                p1 = Point(y, x)
                p2 = Point(y + dy, x + dx)
                p3 = Point(y + 2 * dy, x + 2 * dx)

                if not (0 <= p3.y < len(data) and 0 <= p3.x < len(data[0])):
                    continue

                if data[p2.y][p2.x] == "A" and data[p3.y][p3.x] == "S":
                    mas.append([p1, p2, p3])

# Find MAS with intersecting point in the middle
count = 0
matched: set[Point] = set()

for i, p in enumerate(mas):
    for j, q in enumerate(mas[i + 1 :]):
        if p[1] == q[1] and p[1] not in matched:
            count += 1
            matched.add(p[1])

print(count)
