import os
import re
from enum import Enum

class Mat(Enum):
    AIR = "."
    ROCK = "#"
    SAND = "o"


def print_cave(cave):
    for line in cave:
        print("".join([item.value for item in line]))
    print("".join([f"{i}" for i in range(len(line))]))

grid = [[Mat.AIR for _ in range(1000)] for _ in range(1000)]

lowest_rock = 0
with open(os.getcwd() + "/day14/input.txt", encoding="utf-8") as f:
    lines = map(lambda x: re.findall("\d+,\d+", x), f.read().splitlines())
    for line in lines:
        for y, item in enumerate(line):
            if y == 0:
                continue

            prev_x, prev_y = map(int, line[y - 1].split(","))
            curr_x, curr_y = map(int, item.split(","))

            min_x, max_x = min(prev_x, curr_x), max(prev_x, curr_x)
            min_y, max_y = min(prev_y, curr_y), max(prev_y, curr_y)


            if min_y > lowest_rock:
                lowest_rock = curr_y

            for x in range(min_x, max_x + 1):
                grid[curr_y][x] = Mat.ROCK
            
            for y in range(min_y, max_y + 1):
                grid[y][curr_x] = Mat.ROCK


def move_sand(grid, y: int, x: int):
    while True:
        if grid[y + 1][x] == Mat.AIR:
            y += 1
        else:
            break

    if grid[y + 1][x - 1] == Mat.AIR:
        return move_sand(grid, y + 1, x - 1)
    elif grid[y + 1][x + 1] == Mat.AIR:
        return move_sand(grid, y + 1, x + 1)
    else:
        grid[y][x] = Mat.SAND

    return grid


# Part 1
# i = 0
# while True:
#     try:
#         grid = move_sand(grid, 0, 500)
#         i += 1
#     except:
#         print(i)
#         break


# Part 2: with bottom layer
lowest_rock += 2
for x in range(len(grid[0])):
    grid[lowest_rock][x] = Mat.ROCK

i = 0
while True:
    grid = move_sand(grid, 0, 500)
    i += 1
    if grid[0][500] == Mat.SAND:
        print(i)
        break