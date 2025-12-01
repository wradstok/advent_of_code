import os
import re

with open(os.getcwd() + "/day15/input.txt", encoding="utf-8") as f:
    lines = list(map(lambda x: list(map(int, re.findall("\d+", x))), f.read().splitlines()))

def run_for_line(line_nr: int):
    missing, beacons = set(), set()

    sections = []
    for (s_x, s_y, b_x, b_y) in lines:
        beacons.add((b_y, b_x))

        total = abs(s_x - b_x) + abs(s_y - b_y) 
        dist = abs(s_y - line_nr)
        
        if dist <= total:
            remaining = total - dist
            sections.append((s_x - remaining, s_x + remaining))

    highest_x = 0
    for _, end in sections:
        if end > highest_x:
            highest_x = end
    
    for i in range(highest_x + 1):
        found = False
        for section in sections:
            if i >= section[0] and i <= section[1]:
                found = True
                break
        
        if not found:
            missing.add(i)

    return missing

# Part 1
# print(len(run_for_line(10)))

# Part 2
for i in range(4_000_000):
    if i % 10000 == 0:
        print(i)
    missing = run_for_line(i) 
    
    # missing = [x for x in range(max_x + 1) if x not in found]

    if len(missing) > 0:
        print(list(missing)[0] * 4_000_000 + i)
