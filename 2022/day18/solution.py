import os
import sys

sys.setrecursionlimit(16000)
with open(os.getcwd() + "/day18/input.txt", encoding="utf-8") as f:
    droplets = set(map(lambda x: tuple(map(int, x.split(","))), f.read().splitlines()))


def get_neighbour_cells(pos: tuple) -> list[tuple[int,int,int]]:
    neighbours = []
    for idx in range(3):
        for offset in [-1,1]:
            neighbours.append(tuple(pos + offset if i == idx else pos for i, pos in enumerate(pos)))
    return neighbours


# Part 1
exposed: int = 0
for droplet in droplets:
    adj = get_neighbour_cells(droplet)
    exposed += sum((1 for neighbour in adj if neighbour not in droplets))

print(exposed)

# Part 2
def get_range(grid: set, idx: int) -> tuple:
    return (
        min((pos[idx] for pos in grid)) - 1,
        max((pos[idx] for pos in grid)) + 1
    )

min_x, max_x = get_range(droplets, 0)
min_y, max_y = get_range(droplets, 1)
min_z, max_z = get_range(droplets, 2)

def floodfill(curr: tuple, found: set, lava: set) -> bool:
    found.add(curr)
    
    neighbours = get_neighbour_cells(curr)
    neighbours = [x for x in neighbours if x not in found and curr not in lava]

    for neighbour in neighbours:
        if neighbour[0] < min_x or neighbour[0] > max_x:
            return True
        elif neighbour[1] < min_y or neighbour[1] > max_y:
            return True
        elif neighbour[2] < min_z or neighbour[2] > max_z:
            return True
        else:
            if floodfill(neighbour, found, lava):
                return True

    return False


possible_bubbles = set()
for droplet in droplets:
    adj = get_neighbour_cells(droplet)
    for side in adj:
        if side not in droplets:
            possible_bubbles.add(side)

outside = set()
actual_bubbles = set()
for i, bubble in enumerate(possible_bubbles):
    if bubble not in outside:
        points = set()
        if floodfill(bubble, points, droplets):
            outside = outside.union(points)
        else:
            actual_bubbles = actual_bubbles.union(points)

filled_droplets = droplets.union(actual_bubbles)
exposed: int = 0
for droplet in filled_droplets:
    sides = get_neighbour_cells(droplet)
    exposed += sum((1 for neighbour in sides if neighbour not in filled_droplets))

print(exposed)
