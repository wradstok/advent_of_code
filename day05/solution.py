import re

with open("day05/input.txt") as f:
    lines = f.read().splitlines()

maps = {}
for line in lines[2:]:
    if line == "":
        continue

    if "map" in line:
        curr_map = line.split()[0]
        maps[curr_map] = []
        continue

    # destination, source, range
    triple = list(map(int, re.findall(r"\d+", line)))
    maps[curr_map].append(
        (triple[0], triple[0] + triple[2], triple[1], triple[1] + triple[2])
    )

seeds = []
seed_ranges = list(map(int, re.findall(r"\d+", lines[0])))
for start, length in zip(*(iter(seed_ranges),) * 2):
    seeds.extend(range(start, start + length))


lowest_locations = []
for seed in seeds:
    curr_value = seed
    for mmap in maps.values():
        for dest_start, dest_end, src_start, src_end in mmap:
            if src_start <= curr_value < src_end:
                curr_value = dest_start + (curr_value - src_start)
                break

    lowest_locations.append(curr_value)
print(min(lowest_locations))
a = 2
