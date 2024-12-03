import re

with open("2024/day03/input.txt") as f:
    data = f.read()

mults = re.findall(r"mul\((\d+)\,(\d+)\)", data)

res = 0
for a, b in mults:
    res += int(a) * int(b)

print(res)


operations = re.findall(r"mul\((\d+)\,(\d+)\)|(do\(\))|(don't\(\))", data)

res = 0
enabled = True
for a, b, do, dont in operations:
    if do == "do()":
        enabled = True
    elif dont == "don't()":
        enabled = False
    elif enabled:
        res += int(a) * int(b)
print(res)
