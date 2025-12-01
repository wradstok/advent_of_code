import os

with open(os.getcwd() + "/day17/input.txt", encoding="utf-8") as f:
    jet_pattern = f.read().splitlines()[0]

rocks = [
    [["#", "#", "#", "#"]],
    [[".", "#", "."], ["#", "#", "#"], [".", "#", "."]],
    [["#", "#", "#"], [".", ".", "#"], [".", ".", "#"]],
    [["#"], ["#"], ["#"], ["#"]],
    [["#", "#"], ["#", "#"]],
]


def draw_board(board):
    print("_______")
    for i, line in enumerate(reversed(board)):
        print(f"{len(board) - i}: \t {''.join(line)}")


def is_valid(board: list, rock: list, x_pos: int, y_pos: int) -> bool:
    # Try to move every line
    for i, rock_line in enumerate(rock):
        for j, rock_point in enumerate(rock_line):
            if rock_point == ".":
                continue

            n_x = x_pos + j
            if n_x < 0 or n_x > 6:
                return False

            if board[y_pos + i][n_x] == "#":
                return False
    return True

def update_board(board: list, rock: list, x_pos: int, y_pos: int) -> list:
    for i, rock_line in enumerate(rock):
        for j, rock_point in enumerate(rock_line):
            if rock_point == '#':
                board[y_pos + i][x_pos + j] = rock_point

    return board

def find_highest_block(board):
    for i, line in enumerate(reversed(board)):
        if "#" in line:
            return len(board) - i - 1

full_board = [["#" for _ in range(7)]]

cache = dict()
rock_nr, op_idx = 0, 0

height_skipped = 0
rocks_skipped = 0
has_skipped = False

while True:
    curr_rock = rocks[rock_nr % len(rocks)]

    top = find_highest_block(full_board)

    # Check if the next move we need to make is cached
    cache_key = (op_idx, rock_nr % len(rocks))
    if cache_key in cache:
        prev_height, prev_rock_nr = cache[cache_key]

        rock_diff = rock_nr - prev_rock_nr
        if rock_nr % rock_diff == 1_000_000_000_000 % rock_diff:
            height_diff = top - prev_height

            fits = (1_000_000_000_000 - rock_nr) // rock_diff

            rocks_skipped = fits * rock_diff
            height_skipped = fits * height_diff

            print(f"Height after a gazillion rockfalls: {height_skipped + find_highest_block(full_board)}")
            exit()
    else:
        cache[cache_key] = (top, rock_nr)


    # Make board taller if required
    required_height = top + len(curr_rock) + 4
    if len(full_board) < required_height:
        full_board.extend([
            ["." for _ in range(7)] for _ in range(required_height - len(full_board))
        ])

    x, y = 2, top + 4
    while True:
        operation = jet_pattern[op_idx]
        op_idx = (op_idx + 1) % len(jet_pattern)

        # Check sideways
        X_DIR = - 1 if operation == "<" else 1
        if is_valid(full_board, curr_rock, x + X_DIR, y):
            x += X_DIR

        # Check downwards
        if is_valid(full_board, curr_rock, x, y - 1):
            y -= 1
        else:
            full_board = update_board(full_board, curr_rock, x, y)
            break

    rock_nr += 1
    if rock_nr == 2022:
        print(f"Height after 2022 rocks: {find_highest_block(full_board)}")
