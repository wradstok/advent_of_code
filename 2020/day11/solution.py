from enum import Enum
from copy import deepcopy
from functools import partial
class SeatState(Enum):
    floor = "."
    occupied = "#"
    empty = "L"
    outside = "!"

with open("input.txt") as file:
    seats = file.read().splitlines()

    trans = {i.value: i for i in SeatState}
    seats = list(map(lambda row : list(map(lambda seat: trans[seat], list(row))), seats))

def read_seat(source, x, y):
    # Is it inside the y-range?
    if not 0 <= y < len(source):
        return SeatState.outside

    # Is it inside the x-range?
    if not 0 <= x < len(source[0]):
        return SeatState.outside

    return source[y][x]

def update_seat(seats, x, y, val: SeatState):
    if x == 0:
        seats[y] = [val] + seats[y][1:]
    else:
        seats[y] = seats[y][0:x] + [val] + seats[y][x + 1:]

def get_neighbour_counts_p1(source, x, y):
    neighbours = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i == x and y == j:
                continue
            
            neighbours.append(read_seat(source, i, j))
    
    return neighbours.count(SeatState.occupied)

def get_neighbour_counts_p2(seats, x, y):

    def read_dir(seats, x, y, step_x, step_y):
        # Perform first step
        x, y = x + step_x,  y + step_y

        seat = read_seat(seats, x, y)
        while seat == SeatState.floor:
            x, y = x + step_x,  y + step_y
            seat = read_seat(seats, x, y)

        return seat

    visible = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            visible.append(read_dir(seats, x, y, i, j)) 

    return visible.count(SeatState.occupied)

def iterate(seats, neigh_func, leave_amount):
    next = deepcopy(seats)

    for y, row in enumerate(seats):
        for x, seat in enumerate(row):
            neighbours = neigh_func(seats, x, y)

            if seat == SeatState.empty and neighbours == 0:
                update_seat(next, x, y, SeatState.occupied)
            elif seat == SeatState.occupied and neighbours >= leave_amount:
                update_seat(next, x, y, SeatState.empty)

    return next
    
def count_occupied(seats):
    return sum(map(lambda row: row.count(SeatState.occupied), seats))

# Continue updating until steady-state
while True:
    next = iterate(seats, partial(get_neighbour_counts_p2), 6)
    if seats == next:
        break
    seats = next


print(f"Answer: {count_occupied(seats)}")