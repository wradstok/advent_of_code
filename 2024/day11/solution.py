from collections import defaultdict

with open("2024/day11/input.txt") as f:
    data = f.read().splitlines()[0].split()

    stones: dict[str, int] = defaultdict(int)
    for stone in data:
        stones[stone] += 1

for i in range(75):
    next_stones = defaultdict(int)

    for stone, count in stones.items():
        if stone == "0":
            next_stones["1"] += count
        elif len(stone) % 2 == 0:
            left, right = stone[: len(stone) // 2], stone[len(stone) // 2 :]
            while len(right) > 1 and right[0] == "0":
                right = right[1:]
            next_stones[left] += count
            next_stones[right] += count
        else:
            new_stone = str(int(stone) * 2024)
            next_stones[new_stone] += count

    stones = next_stones

total_stones = 0
for count in next_stones.values():
    total_stones += count
print(total_stones)
