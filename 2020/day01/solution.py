from itertools import combinations

# Part one
expenses = []
with open("input.txt") as file:
    expenses = list(map(int, file.readlines()))

for (a, b) in combinations(expenses, 2):
    if a + b == 2020:
        print(f"Answer: {a * b}")
        break
    
# Part two
for (a, b, c) in combinations(expenses, 3):
    if a + b + c == 2020:
        print(f"Answer: {a * b * c}")
        break
