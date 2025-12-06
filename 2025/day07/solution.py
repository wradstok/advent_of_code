from math import prod
from collections import defaultdict
import re

with open("2025/day07/input.txt") as f:
    lines = f.read().splitlines()

problems = defaultdict(list)
results = []
for line in lines:
    if "*" in line or "+" in line:
        for i, op in enumerate(line.split()):
            if op == "+":
                results.append(sum(problems[i]))
            if op == "*":
                results.append(prod(problems[i]))
    else:
        nums = map(int, line.split())
        for i, num in enumerate(nums):
            problems[i].append(num)

print(sum(results))

### This is all terrible

results = []
opers = list(re.finditer(r"\*|\+", lines[-1]))
for o, curr in enumerate(opers):
    if o < len(opers) - 1:
        section = (curr.span()[0], opers[o + 1].span()[0] - 1)
    else:
        section = (curr.span()[0], len(lines[0]))

    nums = defaultdict(str)
    for c in range(*section):
        for line in lines[:-1]:
            if line[c]:
                nums[c] += line[c]

    p_nums = map(int, nums.values())
    if lines[-1][curr.span()[0]] == "+":
        results.append(sum(p_nums))
    else:
        results.append(prod(p_nums))

print(sum(results))
