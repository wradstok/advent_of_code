with open("2024/day09/input.txt") as f:
    data = f.read().splitlines()[0]

expanded: list[int | str] = []
ids = []
for i, bit in enumerate(data):
    if i % 2 == 0:
        expanded.extend([i // 2] * int(bit))
        ids.append(i // 2)
    else:
        expanded.extend(["."] * int(bit))

# while True:
#     try:
#         free = expanded.index(".")
#         if free == len(expanded) - 1:
#             break

#         last_free = next(i for i in range(free, len(expanded)) if expanded[i] != ".")
#         end_length = expanded[::-1].index(".")

#         sec_length = min(last_free - free, end_length)

#     except ValueError:
#         break

#     start = expanded[:free]
#     section = expanded[: -sec_length - 1 : -1]
#     end = expanded[free + sec_length : -sec_length]

#     expanded = start + section + end
#     while expanded[-1] == ".":
#         expanded.pop()


for block_id in reversed(ids):
    block_start = expanded.index(block_id)
    block_size = expanded.count(block_id)

    size = 0
    for i, val in enumerate(expanded):
        if i > block_start:
            break

        if size == block_size:
            # TIL you can swap slices in lists
            expanded[i - block_size : i], expanded[block_start : block_start + block_size] = (
                expanded[block_start : block_start + block_size],
                expanded[i - block_size : i],
            )
            break
        if val == ".":
            size += 1
        else:
            size = 0


val = 0
for i, char in enumerate(expanded):
    if isinstance(char, int):
        val += i * char

print(val)
