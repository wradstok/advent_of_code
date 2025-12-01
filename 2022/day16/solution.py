import os
import re
from functools import cache
import itertools

graph = dict()
rates = dict()

with open(os.getcwd() + "/day16/input.txt", encoding="utf-8") as f:
    for line in f:
        valves = re.findall("([A-Z]{2})", line)
        graph[valves[0]] = valves[1:]
        rates[valves[0]] = int(re.findall("\d+", line)[0])


# Calculate min distances between all nodes
distances: dict[str, dict[str], int] = {valve: {valve: 0} for valve in graph}
for start in graph:
    stack = [start]
    while len(stack) > 0:
        curr = stack.pop(0)
        for node in graph[curr]:
            if node not in distances[start]:
                stack.append(node)
                distances[start][node] = distances[start][curr] + 1


@cache
def dfs(curr: str, my_slice: frozenset, visited: tuple, time_remaining: int):
    # Substract opening time
    time_remaining -= 1
    if time_remaining == 0:
        return 0

    visited = tuple(list(visited) + [curr])
    options = [
        node
        for node in my_slice if node not in visited
        and rates[node] > 0 and time_remaining - distances[curr][node] > 1
    ]

    scores = [(0, visited)]
    for node in options:
        dist = distances[curr][node]
        scores.append(dfs(node, my_slice, visited, time_remaining - dist))

    best_score, best_visited = max(scores, key=lambda x: x[0])

    return best_score + rates[curr] * time_remaining, best_visited


flow_nodes = [node for node, rate in rates.items() if rate > 0]

pressure, _ = dfs("AA", frozenset(flow_nodes), tuple(), 31)
print(f"Most pressure released by just you {pressure}")


# Part2 .. takes a couple minutes to run :)
partitions = []
for i in range(1, len(flow_nodes)):
    partitions.extend(map(frozenset, itertools.combinations(flow_nodes, i)))

all_scores = dict()
for partition in partitions:
    score, done = dfs("AA", partition, tuple(), 27)
    all_scores[partition] = score

best = 0 
for partition in partitions:
    remain = frozenset(flow_nodes) - partition
    score = all_scores[partition] + all_scores[remain]
    if score > best:
        best = score

print(f"Most pressure released by working together with the elephant {best}")
