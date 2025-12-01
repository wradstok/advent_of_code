def load_bags(baglines):
    options = {} 

    for bagline in baglines:
        # Target bag and its requirements
        bag, reqs = bagline.strip(".").split(" bags contain ")
        
        options[bag] = {}
        if reqs != "no other bags":
            # Parse each requirement
            reqs = reqs.split(", ")
            for req in reqs:
                count, name = bag_parser(req)
                options[bag][name] = count
    return options

def bag_parser(req):
    count = int(req[0])
    name = req[1:].split("bag")[0].strip()
    return count, name


with open("input.txt") as file:
    baglines = file.read().splitlines()

# Part 1
options = load_bags(baglines)
contains_gold = set()

def check_reqs(name):
    reqs = options[name]

    if "shiny gold" in reqs.keys():
        contains_gold.add(name)
        return True
    
    for req in reqs:
        if check_reqs(req):
            return True
    
    return False

valid = 0
for bag in options.keys():
    if bag in contains_gold or check_reqs(bag):
        valid += 1

print(f"Answer: {valid}")

# Part 2
def count(name: str) -> int:
    reqs = options[name]
    
    sum = 0
    for bag, amount in reqs.items():
        sum += amount * (count(bag) + 1)

    return sum

print(f"Answer: {count('shiny gold')}")
