# Turns out a lot of this code wasn't necessary, but you never know what part 2 brings :)
import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class File:
    name: str
    size: int


@dataclass
class Dir:
    subdirs: dict[str, "Dir"]
    files: list[File]
    parent: Optional["Dir"]

    def sum_all_with_max_size(self, at_most: int, found: int) -> int:
        my_size = self.get_size()
        if my_size < at_most:
            found += my_size

        for subdir in self.subdirs.values():
            found = subdir.sum_all_with_max_size(at_most, found)
        return found

    def get_smallest_size(self, at_least: int, best: int) -> int:
        my_size = self.get_size()
        if at_least < my_size < best:
            best = my_size

        for subdir in self.subdirs.values():
            best = subdir.get_smallest_size(at_least, best)

        return best

    def get_size(self) -> int:
        return sum((file.size for file in self.files)) + sum(
            (subdir.get_size() for subdir in self.subdirs.values())
        )


with open(os.getcwd() + "/day07/input.txt") as f:
    lines = f.read().splitlines()

root = Dir({}, [], None)
curr_pos = root

for line in lines:
    match line.split():
        case "$", "cd", "..":
            curr_pos = curr_pos.parent
        case "$", "cd", "/":
            curr_pos = root
        case "$", "cd", name:
            curr_pos = curr_pos.subdirs[name]
        case "$", "ls":
            continue
        case "dir", name:
            curr_pos.subdirs[name] = Dir({}, [], curr_pos)
        case size, name:
            curr_pos.files.append(File(name, int(size)))

print(f"Size of dirs on fs smaller than 100k: {root.sum_all_with_max_size(100000, 0)}")

at_least = 30000000 - (70000000 - root.get_size())
print(f"Smallest to delete has size {root.get_smallest_size(at_least, 70000000)}")
