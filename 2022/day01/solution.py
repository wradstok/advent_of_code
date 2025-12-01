import os

with open(os.getcwd() +  "/day01/input.txt") as f:
    lines = f.read().splitlines()

# Store all elf snacks just in case we need them
elf = []
elf_weights = []
for weight in lines:
    if weight:
        elf.append(int(weight))
    else:  
        elf_weights.append(elf)
        elf = []
elf_weights.append(elf)

# Calculate number of calories each elf is carrying
weights = map(sum, elf_weights)
weights  = sorted(weights, reverse=True)
print(f"Elf with most snacks has {weights[0]} calories")
print(f"Top 3 elves with most snacks have {sum(weights[0:3])} calories")

