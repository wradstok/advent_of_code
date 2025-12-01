from functools import reduce

def fold(func, collection):
    return reduce(lambda x, y: func(x,y), collection)

def count(collection):
    return sum(map(len, collection))

with open("input.txt") as file:
    answers = file.read().splitlines()

# Create the groups, each consists of a list of answer (sets)
curr, groups = [], []
for answer in answers:
    if answer == "":
        groups.append(curr)
        curr = []
    else:
        curr.append(set(answer))

# Add the final group to the list because the final line empty line is ignored.
groups.append(curr)

# Part 1
union_groups = map(lambda z: fold(set.union, z), groups)
print(f"Answer: {count(union_groups)}")
    
# Part 2
intersect_groups = map(lambda z: fold(set.intersection, z), groups)
print(f"Answer: {count(intersect_groups)}")
