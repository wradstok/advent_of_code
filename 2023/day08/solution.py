import re
from dataclasses import dataclass
import math


@dataclass
class Node:
    name: str
    left: str
    right: str


with open("2023/day08/input.txt") as f:
    lines = f.read().splitlines()
    instructions = [*lines[0]]
    nodes = {}
    for line in lines[2:]:
        items = re.findall(r"\w+", line)
        nodes[items[0]] = Node(*items)


def solve(node: str):
    i = 0
    while True:
        instr = instructions[i % len(instructions)]
        match instr:
            case "L":
                node = nodes[node].left
            case "R":
                node = nodes[node].right
        i += 1

        if node.endswith("Z"):
            return i


print(solve("AAA"))

cycles = [solve(node) for node in nodes if node.endswith("A")]
print(math.lcm(*cycles))
