def read_input():
    with open("input.txt") as file:
        lines = list(map(int, file.read().splitlines()))
        return lines[0:25], lines[25:]

def first_number():
    for next in numbers:
        if any(map(lambda x: next in x, sum_sets.values())):
            first_entry = list(sum_sets.keys())[0]
            del sum_sets[first_entry]
            
            for key, sum_set in sum_sets.items():
                sum_set.add(key + next)

            sum_sets[next] = set()

        else:
           return next

    raise Exception

preamble, numbers = read_input()

sum_sets = {}
for i, fst in enumerate(preamble):
    sum_sets[fst] = set()
    for snd in preamble[i + 1:]:
        sum_sets[fst].add(fst + snd)

# Part 1
solution = first_number()
print(f"Answer: {solution}")

# Part 2
# I know, this is not efficient at all, but its instant anyway :)
for window_size in range(2, 50):
    for i in range(0, len(numbers) - window_size):
        subset = numbers[i: i + window_size]
        total = sum(subset)
        
        if total == solution:
            print(f"Answer: {min(subset) + max(subset)}")
            break
