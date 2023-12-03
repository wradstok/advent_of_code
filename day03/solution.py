import re

with open("day03/input.txt") as f:
    lines = f.read().splitlines()


def add_gear(x, y, num):
    gears[f"{x}-{y}"] = gears.get(f"{x}-{y}", []) + [num]


def get_adjacent(x: int, y: int):
    for i in range(-1, 2):
        for j in range(-1, 2):
            xpos, ypos = x + i, y + j
            if not 0 <= xpos < len(line):
                continue
            if not 0 <= ypos < len(lines):
                continue
            yield xpos, ypos


def check_symbols_adjacent(x: int, y: int, num: int):
    for xpos, ypos in get_adjacent(x, y):
        char = lines[ypos][xpos]
        if not char.isdigit() and char != ".":
            if char == "*":
                add_gear(xpos, ypos, num)
            return True
    return False


gears = {}
valid = []
for y, line in enumerate(lines):
    numbers = re.findall(r"(\d+)", line)
    for grp in re.finditer(r"(\d+)", line):
        for x in range(grp.start(), grp.end()):
            if check_symbols_adjacent(x, y, int(grp.group())):
                valid.append(int(grp.group()))
                break

print(sum(valid))

ratios = []
for gear in gears.values():
    if len(gear) == 2:
        ratios.append(gear[0] * gear[1])
print(sum(ratios))
