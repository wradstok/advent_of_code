import re

with open("2023/day09/input.txt") as f:
    lines = f.read().splitlines()
    lines = [list(map(int, line.split())) for line in lines]


def history(line: list[int]) -> list[int]:
    res = []
    for a, b in zip(line, line[1:]):
        res.append(b - a)

    return res


def calc_histories(line: list[int]) -> int:
    ends = [line[-1]]
    while True:
        hist = history(line)
        ends.append(hist[-1])
        line = hist

        if all(x == 0 for x in hist):
            break

    return sum(ends)


extra = []
for line in lines:
    extra.append(calc_histories(line))

print(sum(extra))

extra = []
for line in lines:
    extra.append(calc_histories(line[::-1]))

print(sum(extra))
