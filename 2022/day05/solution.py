import os
import re

commands = []
crates = [[] for i in range(9)]
with open(os.getcwd() +  "/day05/input.txt") as f:
    lines = f.read().splitlines()

    for line in lines:
        if "[" in line:
            for pos, i in enumerate(range(1, len(line), 4)):
                if line[i] != " ":
                    crates[pos].append(line[i])

        elif "move" in line:
            commands.append([int(x) for x in re.findall("\d+", line)])

for (num, orig, dest) in commands:
    orig, dest = orig - 1, dest - 1 
    pickup = crates[orig][0:num]
    # pickup.reverse() # Uncomment for part 1
    crates[dest] = pickup + crates[dest]
    crates[orig] = crates[orig][num:]

tops = [stack[0] for stack in crates if len(stack) > 0]
print("".join(tops))