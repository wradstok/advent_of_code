with open("input.txt") as file:
    timestamp = int(file.readline())
    busses = file.readline().split(',')

def min_wait_time(schedule) -> int:
    min_wait, best_bus = 999999, -1
    for bus in schedule:
        wait = bus - (timestamp % bus)
        if wait < min_wait:
            min_wait, best_bus = wait, bus
    
    return min_wait * best_bus

def earliest_subsequent(schedule) -> int:
    test_val
    while True:
        for bus in busses:
    


print(f"Answer: {min_wait_time(map(int, filter(lambda x: x != 'x', busses)))}")
