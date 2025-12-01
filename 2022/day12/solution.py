import os
import heapq

maze = []
with open(os.getcwd() + "/day12/input.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()
    for i, line in enumerate(lines):
        row = [ord(item) - ord("a") if item not in ["S", "E"] else item for item in line]
        if "S" in row:
            start = (i, row.index("S"))
        if "E" in row:
            end = (i, row.index("E"))

        row = [0 if item == "S" else item for item in row]
        row = [26 if item == "E" else item for item in row]

        maze.append(row)

def get_adjacent(y: int, x: int) -> list[tuple[int]]:
    height = maze[y][x]

    above = (y + 1, x) if y < len(maze) -1 else None
    below = (y - 1, x) if y >= 1 else None
    right = (y, x + 1) if x < len(maze[0]) -1  else None
    left  = (y, x - 1)  if x >= 1 else None
    
    reachable = [pos for pos in [above, below, right, left] if pos is not None]
    reachable = [pos for pos in reachable if maze[pos[0]][pos[1]] in [i for i in range(height + 2)]] 
    return reachable


def dijkstra(maze: list[list[int]], begin: tuple[int, int], final: tuple[int, int]) -> int:
    dist = {(y,x) : 0 if (y,x) == begin else 99999 for x in range(len(maze[0])) for y in range(len(maze))}

    min_heap = [(0, begin)]
    while len(min_heap) > 0:
        _, (y, x) = heapq.heappop(min_heap)
        if y == -1 and x == -1:
            continue  # Encountered an updated item

        if (y, x) == final:
            break  # Early exit

        for adj in get_adjacent(y, x):
            path_length = dist[y,x] + 1
            if path_length < dist[adj]:
                dist[adj] = path_length
                heapq.heappush(min_heap, (path_length, adj))

    return dist[final]


print(f"Best option from S: {dijkstra(maze, start, end)}")

options = [(y, x) for y in range(len(maze)) for x in range(len(maze[0])) if maze[y][x] == 0]

results = [dijkstra(maze, option, end) for option in options]
print(f"Best option from any: {min(results)}")
