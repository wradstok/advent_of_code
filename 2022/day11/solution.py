import os
import re
import math

class Monkey():
    items: list[int]
    test: int

    true_target: int
    false_target: int

    num_inspected: int = 0
    update_str : str

monkeys : list[Monkey] = []
with open(os.getcwd() + "/day11/input.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

    for i, line in enumerate(lines):
        line = line.lstrip()

        if "Monkey" in line:
            monkey = Monkey()

        if line == "":
            monkeys.append(monkey)

        match line.split(":"):
            case "Starting items", items:
                monkey.items = list(map(int, items.split(",")))
            case "Operation", expression:
                monkey.update_str = expression.split("new = old")[1]
            case "Test", test:
                monkey.test = int(re.findall(r"\d+", test)[0])
            case "If true", action:
                monkey.true_target = int(re.findall(r"\d+", action)[0])
            case "If false", action:
                monkey.false_target = int(re.findall(r"\d+", action)[0])
monkeys.append(monkey)

gcd = math.prod((monkey.test for monkey in monkeys))

for iteration in range(10000):
    for i, monkey in enumerate(monkeys):
        while len(monkey.items) > 0:
            item = monkey.items.pop(0)
            monkey.num_inspected += 1

            worry = eval(f"{item} {monkey.update_str.replace('old', str(item))}")
            # worry = worry // 3 # Uncomment for part 1

            worry = worry % gcd
            if worry % monkey.test == 0:
                monkeys[monkey.true_target].items.append(worry)
            else:
                monkeys[monkey.false_target].items.append(worry)


active_levels = sorted([monkey.num_inspected for monkey in monkeys], reverse=True)
highest = math.prod(active_levels[0:2])
print(f"Amount of monkey business {highest}")
