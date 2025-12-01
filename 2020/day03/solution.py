from functools import reduce

def get_world_entry(world, x):
    line = world[0]
    x = x % len(line)
    return line[x]

def traverse(world, x, x_slope, y_slope, trees):
    world = world[y_slope:]
    if len(world) == 0:
        return trees

    x += x_slope

    if get_world_entry(world, x) == "#":
        trees += 1
    return traverse(world, x, x_slope, y_slope, trees)

world = []
with open("input.txt") as file:
    world = file.read().splitlines()

# Part one
trees_hit = traverse(world, 0, 3, 1, 0)
print(f"Answer: {trees_hit}")

# Part two
slopes = [(1, 1), (3,1), (5, 1), (7,1), (1,2)]
results = []
for x_slope, y_slope in slopes:
    results.append(traverse(world, 0, x_slope, y_slope, 0))

# I'm still on python 3.7, so we don't have math.prod
# Instead use reduce to multiply the elements in the list
# https://www.geeksforgeeks.org/python-multiply-numbers-list-3-different-ways/
print(f"Answer: {reduce((lambda x, y: x * y), results)}")