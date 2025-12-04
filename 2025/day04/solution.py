with open("2025/day04/input.txt") as f:
    lines = list(map(list, f.read().splitlines()))


def get_adjacent(lines: list[list[str]], x: int, y: int) -> list[tuple[int, int]]:
    adjacent = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(lines[0]) and 0 <= ny < len(lines):
                if lines[ny][nx] != ".":
                    adjacent.append((nx, ny))
    return adjacent


def find_removable(lines: list[list[str]]) -> list[tuple[int, int]]:
    removable = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "@":
                adj = get_adjacent(lines, x, y)

                if len(adj) < 4:
                    removable.append((x, y))
    return removable


print(len(find_removable(lines)))


removed = 0
while True:
    removable = find_removable(lines)
    if not removable:
        break
    for x, y in removable:
        lines[y][x] = "."
    removed += len(removable)

print(removed)
