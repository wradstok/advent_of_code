from itertools import chain, zip_longest

with open("day14/input.txt") as f:
    lines = f.read().splitlines()
    lines = [list(line) for line in lines]
    height = len(lines)
    width = len(lines[0])


def rotate(lines):
    return list(zip(*reversed(lines)))


# Insane shift just for fun
def shift_north(rocks):
    return list(
        zip(
            *[
                list(
                    chain(
                        *chain(
                            *zip_longest(
                                map(lambda x: sorted(x, reverse=True), "".join(col).split("#")), [], fillvalue="#"
                            )
                        )
                    )
                )[:-1]
                for col in zip(*rocks)
            ]
        ),
    )


def get_load(rocks):
    load = 0
    for y, row in enumerate(rocks):
        for col in row:
            if col == "O":
                load += height - y
    return load


# Part 1
# print(get_load(shift_north(lines)))


# Part 2
def semi_cycle(rocks):
    rocks = shift_north(rocks)
    rocks = rotate(rocks)
    return rocks


def cycle(rocks):
    rocks = semi_cycle(rocks)
    rocks = semi_cycle(rocks)
    rocks = semi_cycle(rocks)
    rocks = semi_cycle(rocks)

    return rocks


cycles = 1_000_000_000
hashes = {}
i = 0
cycled = False
while True:
    if i == cycles:
        break

    h = hash(tuple(map(tuple, lines)))

    # We reached a cycle, we can fast forward
    if h in hashes and not cycled:
        period = i - hashes[h]
        print(f"Cycle found of size {period} at {i}")

        remaining = cycles - i
        i += remaining // period * period
        cycled = True
        continue

    hashes[h] = i
    lines = cycle(lines)

    i += 1


print(get_load(lines))
