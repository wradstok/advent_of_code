import os

with open(os.getcwd() +  "/day06/input.txt") as f:
    line = f.read().splitlines()[0]

def find(msg: str, size: int) -> int:
    seen = []
    for i, char in enumerate(msg):
        seen.append(char)
        if len(seen) > size:
            seen = seen[1:]
        
        if len(set(seen)) == size:
            return i + 1

print(find(line, 4))
print(find(line, 14))