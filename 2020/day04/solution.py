import re

# These could be a lot prettier with the assignment expressions from python 3.8
valid_rules = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020 ,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: ("cm" in x or "in" in x) and (150 <= int(x[:-2]) <= 193 if "cm" in x else 59 <= int(x[:-2]) <= 76),
    "hcl": lambda x: len(re.findall(r'^#(\d|[a-f]){6}$', x)) == 1,
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: len(re.findall(r"^\d{9}$", x)) == 1,
    "cid": lambda x: True,
}

def is_valid(passport: dict, perform_validation: bool):
    prop_count = len(passport)
    simple = prop_count == 8 or (prop_count == 7 and not passport.__contains__("cid"))
    
    if not perform_validation:
        return simple 
    
    results = []
    for key, val in passport.items():
        res = valid_rules[key](val)
        results.append(res)
    return simple and all(results)

with open("input.txt") as file:
    lines = file.read().splitlines()

passports, curr = [], {}
for line in lines:
    if line == "":
        # End of current passport
        passports.append(curr)
        curr = {}
    else:
        # Add to current passport
        props = line.split()

        for prop in props:
            key, val = prop.split(":")
            curr[key] = val 

# The final line does not load properly as a newline even though it is in the file
# So we manually add the current (last) passport
passports.append(curr)

valid_1, valid_2 = 0, 0
for passport in passports:
    if is_valid(passport, False):
        valid_1 += 1
    if is_valid(passport, True):
        valid_2 += 1

# Part 1
print(f"Answer: {valid_1}")

# Part 2
print(f"Answer: {valid_2}")
