from ast import literal_eval
from collections import namedtuple
from typing import TypedDict

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
