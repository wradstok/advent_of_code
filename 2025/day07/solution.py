from collections import defaultdict
from functools import cache

with open("2025/day07/input.txt") as f:
    lines = f.read().splitlines()

splitters: set[tuple[int, int]] = set()
beam_starts = set()
all_beams = set()

for new_y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "S":
            beam_starts.add((x, new_y))
        if char == "^":
            splitters.add((x, new_y))

splits = 0
# while True:
#     new_beam_starts = set()
#     for x, y in beam_starts:
#         for new_y in range(y + 1, len(lines)):
#             if (x, new_y) in all_beams:
#                 break

#             if (x, new_y) in splitters:
#                 is_split = False
#                 for diff in [-1, 1]:
#                     pos = (x + diff, new_y)
#                     if pos in all_beams:
#                         continue

#                     new_beam_starts.add(pos)
#                     all_beams.add(pos)
#                     is_split = True

#                 if is_split:
#                     splits += 1
#                 break

#             all_beams.add((x, new_y))

#     if not new_beam_starts:
#         break
#     beam_starts = new_beam_starts

# print(splits)

beams: dict[tuple[int, int], int] = defaultdict(int)
for beam in beam_starts:
    beams[beam] = 0


@cache
def do(pos: tuple[int, int], splitters) -> int:
    res = 0
    x, y = pos

    for new_y in range(y + 1, len(lines)):
        if new_y == len(lines) - 1:
            return 1

        if (x, new_y) in splitters:
            for diff in [-1, 1]:
                new_pos = (x + diff, new_y)
                res += do(new_pos, splitters)
            break

    return res


c = frozenset(splitters)

print(do(list(beam_starts)[0], c))
