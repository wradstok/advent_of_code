import os

elf_ranges = []
with open(os.getcwd() +  "/day04/input.txt") as f:
    lines = f.read().splitlines()
    for line in lines:
        elves = line.split(",")
        for elf in elves:
            elf_ranges.append(list(map(int, elf.split("-"))))

# Part 1
num_contained = 0
for i in range(len(elf_ranges) // 2):
    fst, snd = elf_ranges[i * 2], elf_ranges[i * 2 + 1]
    if fst[0] >= snd[0] and fst[1] <= snd[1]:
        num_contained += 1
    elif snd[0] >= fst[0] and snd[1] <= fst[1]:
        num_contained += 1
print(f"{num_contained} elf pairs have one cleanup area completely contained in the other")

# Part 2
num_contained = 0
for i in range(len(elf_ranges) // 2):
    fst, snd = elf_ranges[i * 2], elf_ranges[i * 2 + 1]
    fst = set([i for i in range(fst[0], fst[1] + 1)])
    snd = set([i for i in range(snd[0], snd[1] + 1)])
    if len(fst.intersection(snd)) > 0:
        num_contained +=1

print(f"{num_contained} elf pairs have overlap in their cleanup areas")
