with open("2024/day01/input.txt") as f:
    lines = f.readlines()
    left, right = [], []
    for line in lines:
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

left = sorted(left)
right = sorted(right)

diff = 0
for one, two in zip(left, right):
    diff += abs(one - two)

print(diff)

sim = 0
for score in left:
    sim += score * right.count(score)

print(sim)
