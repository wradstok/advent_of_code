from typing import Tuple, List

# Part 1
Password = Tuple[int, int, str, str]

def read_pass(line : str) -> Password:
    counts, letter, pwd = line.split()
    min_size, max_size = map(int, counts.split("-"))
    return min_size, max_size, letter[0], pwd

passwords : List[Password] = []
with open("input.txt") as file:
    passwords = list(map(read_pass, file.read().splitlines()))

valid = 0
for min_size, max_size, letter, pwd in passwords:
    if min_size <= pwd.count(letter) <= max_size:
        valid += 1

print(f"Answer: {valid}")

# Part 2
valid = 0
for fst_pos, snd_pos, letter, pwd in passwords:
    fst = pwd[fst_pos - 1] == letter
    snd = pwd[snd_pos - 1] == letter
    #Xor
    if (fst or snd) and not (fst and snd):
        valid += 1

print(f"Answer: {valid}")

    