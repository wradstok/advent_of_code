from itertools import product

with open("2024/day07/input.txt") as f:
    data = f.read().splitlines()

    targets, values = [], []
    for line in data:
        target, vals = line.split(":")
        targets.append(int(target))
        values.append(list(map(int, vals.split())))

ops = ["*", "+", "||"]
calibration = 0
for target, vals in zip(targets, values):
    options = list(product(ops, repeat=len(vals) - 1))

    for option in options:
        res = vals[0]
        for i, val in enumerate(vals[1:]):
            match option[i - 1]:
                case "+":
                    res += val
                case "*":
                    res *= val
                case "||":
                    res = int(str(res) + str(val))

        if res == target:
            calibration += target
            break

print(calibration)
