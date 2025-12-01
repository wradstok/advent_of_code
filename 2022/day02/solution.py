import os

order = ["A", "B", "C"]


lookup = {
    "X": "A", # Lose
    "Y": "B", # Draw
    "Z": "C", # Win
}
with open(os.getcwd() +  "/day02/input.txt") as f:
    games = map(lambda x: x.split(), f.read().splitlines())
    games = [(game[0], lookup[game[1]]) for game in games]

# Part 1
def wins_against(move):
    res = order.index(move) - 1
    if res == -1:
        res = 2
    return order[res]

def loses_from(move):
    res = order.index(move) + 1
    if res == 3:
        res = 0
    return order[res]

points = 0
for game in games:
    points += order.index(game[1]) + 1
    if game[0] == game[1]:
        points += 3
    if game[0] == wins_against(game[1]):
        points += 6

print(points)

# Part 2
def find_move(opp_move, res):
    if res == "B": # draw
        return opp_move
    if res == "A": # Lose
        return wins_against(opp_move)
    return loses_from(opp_move)

points = 0
for game in games:
    move = find_move(game[0], game[1])
    points += order.index(move) + 1
    if game[1] == "B":
        points += 3
    if game[1] == "C":
        points += 6

print(points)

