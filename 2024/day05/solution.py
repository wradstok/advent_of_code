from collections import defaultdict

with open("2024/day05/input.txt") as f:
    rules, updates = defaultdict(list), []
    for line in f.read().splitlines():
        if "|" in line:
            a, b = line.split("|")
            rules[a].append(b)
        elif "," in line:
            updates.append(line.split(","))


def is_valid(update: list[str]) -> bool:
    for i, page in enumerate(update):
        need = rules[page]
        for item in need:
            if item in update[:i]:
                return False
    return True


def get_middle_sum(updates: list[list[str]]) -> int:
    middle_sum = 0
    for update in updates:
        middle_sum += int(update[len(update) // 2])
    return middle_sum


valid_updates = []
invalid_updates = []
for update in updates:
    if is_valid(update):
        valid_updates.append(update)
    else:
        invalid_updates.append(update)


print(get_middle_sum(valid_updates))

fixed = []
for update in invalid_updates:
    re_ordered = update.copy()

    while True:
        for i, page in enumerate(re_ordered):
            need = rules[page]
            for item in need:
                if item in re_ordered[:i]:
                    re_ordered.remove(item)
                    re_ordered.insert(i, item)
                    break

        if is_valid(re_ordered):
            fixed.append(re_ordered)
            break

print(get_middle_sum(fixed))
