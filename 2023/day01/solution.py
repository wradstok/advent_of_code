import re

with open("2023/day01/input.txt", "r") as f:
    lines = f.readlines()

# Part 1
vals = []
for line in lines:
    digits = re.findall(r"\d", line)
    vals.append(digits[0] + digits[-1])
print(sum(map(int, vals)))

# Part 2
words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

vals = []
for line in lines:
    digits = re.findall(rf"(?=(\d|{'|'.join(words.keys())}))", line)
    digits = [words[digit] if digit in words else digit for digit in digits]
    vals.append(digits[0] + digits[-1])
print(sum(map(int, vals)))
