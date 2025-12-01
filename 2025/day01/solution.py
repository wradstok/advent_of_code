with open("2025/day01/input.txt", "r") as f:
    lines = f.read().splitlines()

rots = []
for line in lines:
    rots.append((line[0], int(line[1:])))

pos = 50
clicks = 0

for rot in rots:
    direction, steps = rot

    clicks += abs(steps // 100)
    steps = steps % 100

    if direction == "L":
        new_pos = pos - steps
    elif direction == "R":
        new_pos = pos + steps

    turned = not 0 < new_pos < 100
    new_pos = new_pos % 100

    if pos != 0:
        if new_pos == 0 or turned:
            clicks += 1

    pos = new_pos


print(clicks)
