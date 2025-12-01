import os

with open(os.getcwd() + "/day10/input.txt") as f:
    lines = f.read().splitlines()

signal_strength = 0
cycle, register = 0, 1
screen = [["." for _ in range(40)] for _ in range(6)]

def add_sig_str(cycle: int, x: int) -> int:
    if cycle in [20, 60, 100, 140, 180, 220]:
        return cycle * x
    return 0

def update_board(board: list[list[int]], register: int, iteration: int):
    crt_x, crt_y = iteration % 40, iteration // 40 
    sprite_x = register % 40

    if crt_x == sprite_x or crt_x == sprite_x - 1 or crt_x == sprite_x + 1:
        board[crt_y][crt_x] = "#"
    return board


for line in lines:
    match line.split():
        case ["noop"]:
            screen = update_board(screen, register, cycle)
            cycle += 1
            signal_strength += add_sig_str(cycle, register)
        case "addx", amount:
            for i in range(2):
                screen = update_board(screen, register, cycle)
                cycle += 1
                signal_strength += add_sig_str(cycle, register)
                
            register += int(amount)
            screen = update_board(screen, register, cycle)

print(signal_strength)

for line in screen:
    print(line)