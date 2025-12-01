from typing import Dict, List, Tuple
from itertools import takewhile

with open("input.txt") as file:
    lines = file.read().splitlines()
    adapters = sorted(list(map(int, lines)), reverse=True)

def calc_power(curr_power: int, differences: List, adapters: List) -> Tuple[int, List]:
    next_power = adapters.pop()
    diff = next_power - curr_power

    # Difference is too great
    if diff > 3:
        return curr_power + 3, differences
    
    differences.append(diff)

    # Out of adapters
    if len(adapters) == 0:
        return curr_power + 3, differences
    
    return calc_power(next_power, differences, adapters)

jolts, differences = calc_power(0, [], adapters.copy())
one_count   = differences.count(1)
three_count = differences.count(3) + 1 # Always one '3' difference for the device.

print(f"Answer: {one_count * three_count}")

# Stores # possible arrangements from a specific joltage
paths: Dict[int, int] = {}

def arrangements(curr_power: int, adapters: List) -> int:
    if adapters == []:
        paths[curr_power] = 1
    else:
        count = 0
        for i, adapter in enumerate(takewhile(lambda x: x - curr_power <= 3, adapters)):
            if adapter not in paths:
                paths[adapter] = arrangements(adapter, adapters[i + 1:].copy())
            
            count += paths[adapter]
        
        paths[curr_power] = count

    return paths[curr_power]


print(f"Answer: {arrangements(0, list(reversed(adapters)))}")