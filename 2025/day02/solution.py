with open("2025/day02/input.txt", "r") as f:
    line = f.read().splitlines()[0].split(",")

ranges = []
for section in line:
    ranges.append(tuple(map(int, section.split("-"))))


def is_repeating(n: str) -> bool:
    return n[0 : len(n) // 2] == n[len(n) // 2 :]


def is_mult_repeating(n: str) -> bool:
    substrs = []
    for i in range(0, len(n) // 2 + 1):
        substrs.append(n[0:i])

    for substr in substrs:
        if n.count(substr) * len(substr) == len(n):
            return True
    return False


invalid = 0
for start, end in ranges:
    for number in range(start, end + 1):
        n = str(number)
        # if is_repeating(n):
        if is_mult_repeating(n):
            invalid += number


print(invalid)
