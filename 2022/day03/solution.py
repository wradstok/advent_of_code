import os

with open(os.getcwd() +  "/day03/input.txt") as f:
    lines = f.read().splitlines()

res = 0
for line in lines:
    middle = len(line) // 2
    first, second = set(line[0:middle]), set(line[middle:])
    chars = first.intersection(second)
    for char in chars:
        res += ord(char) - 38 if char.isupper() else ord(char) - 96

print(f"Sum of priorities is {res}")

res = 0
for i in range(len(lines) // 3):
    badges = set.intersection(*map(set, lines[i * 3 : i * 3 + 3]))
    for badge in badges:
        res += ord(char) - 38 if char.isupper() else ord(char) - 96

print(f"Sum of priorities is {res}")