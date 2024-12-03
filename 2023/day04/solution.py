import re

with open("2023/day04/example.txt") as f:
    lines = f.read().splitlines()
    lines = [line[8:].split("|") for line in lines]

points = []
copies = {i: 1 for i in range(len(lines))}

for i, (win, have) in enumerate(lines):
    win = set(re.findall(r"(\d+)", win))
    have = set(re.findall(r"(\d+)", have))

    match = win.intersection(have)
    if len(match) > 0:
        points.append(1 * 2 ** (len(match) - 1))
        for j in range(len(match)):
            copies[i + j + 1] += copies[i]

print(sum(points))
print(sum(copies.values()))
