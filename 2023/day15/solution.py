from functools import reduce

with open("2023/day15/input.txt") as f:
    seq = f.read().splitlines()[0].split(",")


def do_hash(target: str):
    return reduce(lambda val, c: ((val + ord(c)) * 17) % 256, target, 0)


assert do_hash("HASH") == 52

# Part 1
res = 0
for code in seq:
    res += do_hash(code)
print(res)

# Part 2
boxes = {x: {} for x in range(256)}
for code in seq:
    if "=" in code:
        label, lens = code.split("=")
        box_id = do_hash(label)

        boxes[box_id][label] = int(lens)
    else:
        label = code[:-1]
        box_id = do_hash(label)
        if label in boxes[box_id]:
            del boxes[box_id][label]

power = 0
for box_id, content in boxes.items():
    for lens_id, lens in enumerate(content.values()):
        power += (1 + box_id) * (1 + lens_id) * lens

print(power)
