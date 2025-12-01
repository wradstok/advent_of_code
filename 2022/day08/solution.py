import os
import math

with open(os.getcwd() + "/day08/input.txt") as f:
    r_lines = f.read().splitlines()
    lines = []
    for line in r_lines:
        lines.append([int(x) for x in line])

# PART 1
visible_trees = set()
for y, line in enumerate(lines):
    highest = -1
    for x, item in enumerate(line):
        if item > highest:
            highest = item
            visible_trees.add(tuple((y, x)))
            
    highest = -1
    for x in range(len(line)):
        x_n = len(line) - x - 1
        if line[x_n] > highest:
            highest = line[x_n]
            visible_trees.add(tuple((y, x_n)))

for x in range(len(lines[0])):
    highest = -1
    for y in range(len(lines)):
        if lines[y][x] > highest:
            highest = lines[y][x]
            visible_trees.add(tuple((y, x)))
            
for x in range(len(lines[0])):
    highest = -1
    for y in range(len(lines)):
        y_n  = len(lines) - y - 1
        if lines[y_n][x] > highest:
            highest = lines[y_n][x]
            visible_trees.add(tuple((y_n, x)))
            
print(len(visible_trees))

# PART 2
def get_scenic_score(y: int, x: int) -> int:
    height = lines[y][x]
    res = []

    for i in range(x + 1, len(lines[0])):
        if lines[y][i] >= height:
            res.append(i - x)
            break
    if len(res) == 0:
        res.append(len(lines[0]) -x -1)

    for i in range(x - 1, -1, -1):
        if lines[y][i] >= height:
            res.append(x - i)
            break
    if len(res) == 1:
        res.append(x)

    for j in range(y + 1, len(lines)):
        if lines[j][x] >= height:
            res.append(j - y)
            break
    if len(res) == 2:
        res.append(len(lines) - y -1)

    for j in range(y - 1, -1, -1):
        if lines[j][x] >= height:
            res.append(y - j)
            break
    if len(res) == 3:
        res.append(y)

    return math.prod(res)

results = []
for y in range(len(lines)):
    for x in range(len(lines[0])):
        results.append(get_scenic_score(y, x))

print(max(results))