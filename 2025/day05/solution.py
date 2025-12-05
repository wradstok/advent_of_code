with open("2025/day05/input.txt") as f:
    lines = f.read().splitlines()

ranges = []
ingredients = []
for line in lines:
    if not line:
        continue
    if "-" in line:
        start, end = line.split("-")
        ranges.append((int(start), int(end)))
    else:
        ingredients.append(int(line))

num_fresh = 0
for ingredient in ingredients:
    for r in ranges:
        if r[0] <= ingredient <= r[1]:
            num_fresh += 1
            break
print(num_fresh)


def has_overlap(r1, r2):
    return starts_inside(r1, r2) or ends_inside(r1, r2)


def starts_inside(r1, r2):
    if r2[0] <= r1[0] <= r2[1]:
        return True
    return False


def ends_inside(r1, r2):
    if r2[0] <= r1[1] <= r2[1]:
        return True
    return False


ranges: set[tuple[int, int]] = set(ranges)

while True:
    new_items = set()

    has_merged = set()
    for a in ranges:
        if a in has_merged:
            continue
        to_merge = [a]
        for b in ranges:
            if a == b:
                continue
            if has_overlap(a, b):
                to_merge.append(b)

        has_merged.update(to_merge)
        lowest = min(a[0] for a in to_merge)
        highest = max(a[1] for a in to_merge)

        new_items.add((lowest, highest))

    if len(new_items) == len(ranges):
        break
    ranges = new_items

print(sum(b[1] - b[0] + 1 for b in ranges))
