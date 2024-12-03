import random
import math

nodes = set()
edges = set()

for line in open("2023/day25/input.txt"):
    key, value = line.split(":")

    nodes.add(key)
    for v in value.split():
        nodes.add(v)
        edges.add((key, v))

while True:
    partitions, partition_map = {}, {}
    for i, node in enumerate(nodes):
        partitions[i] = {node}
        partition_map[node] = i

    while len(partitions) > 2:
        u, v = random.choice(list(edges))

        p1, p2 = partition_map[u], partition_map[v]
        if p1 == p2:
            continue

        for node in partitions[p2]:
            partition_map[node] = p1
        partitions[p1].update(partitions[p2])
        del partitions[p2]

    # If we have 3 edges in diferent partitions, we're done
    cut = 0
    for u, v in edges:
        if partition_map[u] != partition_map[v]:
            cut += 1
    if cut == 3:
        print(math.prod(map(len, partitions.values())))
        break
