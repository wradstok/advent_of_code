import re
import math

with open("day02/input.txt", "r") as f:
    lines = f.read().splitlines()
    games = [line[8:].split(";") for line in lines]


limits = {"red": 12, "green": 13, "blue": 14}
valid_games, powers = [], []

for i, game in enumerate(games):
    is_valid = True
    least = {"red": 0, "green": 0, "blue": 0}

    for move in game:
        items = re.findall(r"(\d+) (\w+)", move)

        for amount, color in items:
            least[color] = max(least[color], int(amount))
            if int(amount) > limits[color]:
                is_valid = False

    powers.append(math.prod(least.values()))
    if is_valid:
        valid_games.append(i + 1)

print(sum(powers))
print(sum(valid_games))
