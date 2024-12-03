import re
import math

with open("2023/day06/input.txt") as f:
    lines = f.read().splitlines()
    times = re.findall(r"\d+", lines[0])
    dists = re.findall(r"\d+", lines[1])

# Part 1
wins = []
for time, dist in zip(map(int, times), map(int, dists)):
    win = [speed for speed in range(time) if speed * (time - speed) > dist]
    wins.append(len(win))

print(math.prod(wins))

# Part 2
total_time = int("".join(times))
total_dist = int("".join(dists))

wins = 0
for speed in range(total_time):
    if speed * (total_time - speed) > total_dist:
        wins += 1
print(wins)
