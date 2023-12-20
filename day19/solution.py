from ast import literal_eval
from collections import namedtuple
from typing import TypedDict
import math

with open("day19/input.txt") as f:
    lines = f.read().splitlines()
    workflows, parts = {}, []
    for line in lines:
        if line == "":
            continue
        if line.startswith("{"):
            parts.append(literal_eval(line.replace("{", "{'").replace(",", ",'").replace("=", "':")))
        else:
            label, expr = line.split("{")
            workflows[label] = expr.replace("}", "").split(",")


def do_workflow(part, workflow):
    for rule in workflow[:-1]:
        if "<" in rule:
            about, rest = rule.split("<")
            condition, target = rest.split(":")

            if part[about] < int(condition):
                return target
        else:
            about, rest = rule.split(">")
            condition, target = rest.split(":")
            if part[about] > int(condition):
                return target

    return workflow[-1]


# Part 1
accepted = []
for part in parts:
    workflow = workflows["in"]
    res = do_workflow(part, workflow)
    while True:
        if res == "A":
            accepted.append(part)
            break
        if res == "R":
            break
        res = do_workflow(part, workflows[res])

total = 0
for acc in accepted:
    total += acc["x"] + acc["m"] + acc["a"] + acc["s"]
print(total)


# Part 2
PartRange = namedtuple("PartRange", ["min", "max"])


class XMAS(TypedDict):
    x: PartRange
    m: PartRange
    a: PartRange
    s: PartRange


def workflow_ranges(workflow, xmas: XMAS) -> list[XMAS]:
    other = xmas.copy()

    valid = []
    for rule in workflow[:-1]:
        curr = other.copy()
        if "<" in rule:
            about, rest = rule.split("<")
            condition = rest.split(":")[0]

            curr[about] = PartRange(curr[about].min, int(condition) - 1)
            other[about] = PartRange(int(condition), other[about].max)

        elif ">" in rule:
            about, rest = rule.split(">")
            condition = rest.split(":")[0]

            curr[about] = PartRange(int(condition) + 1, curr[about].max)
            other[about] = PartRange(other[about].min, int(condition))

        match rule.split(":")[-1]:
            case "A":
                valid.append(curr)
            case "R":
                pass
            case target:
                valid.extend(workflow_ranges(workflows[target], curr))

    match workflow[-1]:
        case "A":
            valid.append(other)
        case "R":
            pass
        case target:
            valid.extend(workflow_ranges(workflows[target], other))

    return valid


init_range: XMAS = {
    "x": PartRange(1, 4000),
    "m": PartRange(1, 4000),
    "a": PartRange(1, 4000),
    "s": PartRange(1, 4000),
}
res = workflow_ranges(workflows["in"], init_range)

total = 0
for xmas in res:
    if all(xmas[part].min < xmas[part].max for part in xmas):
        local = [xmas[part].max - xmas[part].min + 1 for part in xmas]
        total += math.prod(local)
print(total)
