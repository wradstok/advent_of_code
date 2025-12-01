import os
import ast
from functools import cmp_to_key
import math

signals = []
with open(os.getcwd() + "/day13/input.txt", encoding="utf-8") as f:
    signals = list(map(ast.literal_eval, [line for line in f.read().splitlines() if line != ""]))

def check_order(left: int|list, right: int|list) -> bool|None:
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        return left < right

    if isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            res = check_order(left[i], right[i])
            if res != None:
                return res
        
        if len(left) == len(right):
            return None
        return len(left) <= len(right)

    if isinstance(left, int):
        return check_order([left], right)

    if isinstance(right, int):
        return check_order(left, [right])

ordered = []
for i, idx in enumerate(range(len(signals) // 2)):
    fst, snd = signals[idx* 2], signals[idx * 2 + 1]
    if check_order(fst, snd):
        ordered.append(i + 1)

print(sum(ordered))


distress_signals = [[[2]], [[6]]]
signals.extend(distress_signals)

result = sorted(signals, key=cmp_to_key(lambda a, b: int(check_order(a, b)) - 1), reverse=True)
locations = [1 + result.index(signal) for signal in distress_signals]


print(math.prod(locations))


