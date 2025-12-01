def decode(remaining: str, lower: int, upper: int):
    if remaining == "":
        return lower 

    head  = remaining[0]
    middle = int((lower + upper) / 2)

    if head == "F" or head == "L":
        # Keep lower half of interval
        lower, upper = lower, middle
    elif head == "B" or head == "R":
        # Keep upper half of interval
        lower, upper = middle + 1, upper
    
    return decode(remaining[1:], lower, upper)
    	
with open("input.txt") as file:
    passes = file.read().splitlines()

# Part 1
seats = set()
for boarding_pass in passes:
    row = decode(boarding_pass[0:7], 0, 127)
    col = decode(boarding_pass[7:], 0, 7)
    seats.add(row * 8 + col)

min_seat, max_seat = min(seats), max(seats)
print(f"Answer: {max_seat}")

# Part 2
for seat in set(range(min_seat, max_seat + 1)).difference(seats):
    if seat - 1 in seats and seat + 1 in seats:
        print(f"Answer: {seat}")