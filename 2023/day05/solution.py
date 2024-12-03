import re

with open("2023/day05/input.txt") as f:
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
    maps[curr_map].append((triple[0], triple[0] + triple[2], triple[1], triple[1] + triple[2]))

# Part 1
seeds = list(map(int, re.findall(r"\d+", lines[0])))
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

# Part 2
ranges = []
seed_ranges = list(map(int, re.findall(r"\d+", lines[0])))
for start, length in zip(*(iter(seed_ranges),) * 2):
    ranges.append((start, start + length))

for mmap in maps.values():
    next_ranges = []
    for start, end in ranges:
        mapped_ranges = []
        for dest_start, dest_end, src_start, src_end in mmap:
            overlap_begin = max(start, src_start)
            overlap_end = min(end, src_end)

            if overlap_begin < overlap_end:
                # There is some overlap that we can map to the next range
                map_start = dest_start - src_start + overlap_begin
                map_end = dest_end - src_end + overlap_end
                next_ranges.append((map_start, map_end))
                mapped_ranges.append((overlap_begin, overlap_end))

        # if never mapped, just add the range
        if len(mapped_ranges) == 0:
            next_ranges.append((start, end))
            continue

        # otherwise we need to add the ranges that were not mapped
        map_start = min(map(lambda x: x[0], mapped_ranges))
        map_end = max(map(lambda x: x[1], mapped_ranges))

        if map_start > start:
            next_ranges.append((start, map_start))
        if map_end < end:
            next_ranges.append((map_end, end))

    ranges = next_ranges

lowest = 90382910382903812903102  # big number
for start, end in ranges:
    if start < lowest:
        lowest = start
print(lowest)
