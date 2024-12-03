from functools import cache

with open("2023/day12/input.txt") as f:
    lines = f.read().splitlines()
    springs, configs = [], []
    for line in lines:
        s, c = line.split()
        springs.append(s)
        configs.append(list(map(int, c.split(","))))


@cache
def fast_check(spring: str, config: tuple[int]):
    if len(spring) == 0:
        if len(config) == 0:
            return 1
        return 0

    match spring[0]:
        case ".":
            # Does nothing, jump to the next point that isn't a `.`
            return fast_check(spring.lstrip("."), config)
        case "#":
            if len(config) == 0 or len(spring) < config[0]:
                return 0

            # Remove the # and check if we can continue
            start, end = spring[: config[0]], spring[config[0] :]
            if "." in start:
                return 0

            # If there is an end part, it must start with a "." to designate the
            # end of this section
            if len(end) > 0:
                if end[0] == "#":
                    return 0
                return fast_check("." + end[1:], config[1:])

            return fast_check("", config[1:])

        case "?":
            # We can pretend this is a # or a .
            return fast_check("#" + spring[1:], config) + fast_check("." + spring[1:], config)


# Part 1
valid = 0
for spring, config in zip(springs, configs):
    valid += fast_check(spring, tuple(config))
print(valid)

# Part 2
valid = 0
for spring, config in zip(springs, configs):
    spring = "?".join([spring] * 5)
    config = tuple(config * 5)

    valid += fast_check(spring, config)
print(valid)
