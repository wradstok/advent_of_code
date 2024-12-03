from collections import namedtuple, defaultdict

with open("2023/day22/input.txt") as f:
    lines = f.read().splitlines()

Brick = namedtuple("Brick", ["x", "y", "z"])

label_to_bricks: dict[int, list[Brick]] = defaultdict(lambda: [])
all_bricks: set[Brick] = set()

for i, line in enumerate(lines):
    fst, snd = line.split("~")

    begin = Brick(*map(int, fst.split(",")))
    end = Brick(*map(int, snd.split(",")))
    for x in range(begin.x, end.x + 1):
        for y in range(begin.y, end.y + 1):
            for z in range(begin.z, end.z + 1):
                label_to_bricks[i].append(Brick(x, y, z))
                all_bricks.add(Brick(x, y, z))


def touch_grass(label: int) -> bool:
    z_coords = [brick.z for brick in label_to_bricks[label]]
    return any(z == 1 for z in z_coords)


def can_fall(label: int, all_bricks: set[Brick]) -> bool:
    if touch_grass(label):
        return False

    for brick in label_to_bricks[label]:
        lower = Brick(brick.x, brick.y, brick.z - 1)

        if lower in all_bricks:
            if lower not in label_to_bricks[label]:
                return False

    return True


while True:
    falling = False
    for label in label_to_bricks:
        if can_fall(label, all_bricks):
            falling = True
            new_big_brick: list[Brick] = []
            for brick in label_to_bricks[label]:
                new_brick = Brick(brick.x, brick.y, brick.z - 1)
                new_big_brick.append(new_brick)

                all_bricks.remove(brick)
                all_bricks.add(new_brick)

            label_to_bricks[label] = new_big_brick

    if not falling:
        break


supported_by: dict[int, set[int]] = {}
for label in label_to_bricks:
    for brick in label_to_bricks[label]:
        lower = Brick(brick.x, brick.y, brick.z - 1)

        if lower not in all_bricks:
            continue

        for other_label in label_to_bricks:
            if other_label == label:
                continue
            if lower in label_to_bricks[other_label]:
                items = supported_by.get(label, set())
                items.add(other_label)
                supported_by[label] = items

total_falling = 0
for label in label_to_bricks:
    all_falling = set([label])

    while True:
        new_falling = all_falling.copy()

        for brick, supports in supported_by.items():
            if len(supports - all_falling) == 0:
                new_falling.add(brick)

        if new_falling == all_falling:
            total_falling += len(all_falling) - 1
            break
        all_falling.update(new_falling)

print(total_falling)
