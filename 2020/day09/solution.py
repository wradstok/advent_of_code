from typing import Set, Tuple

def load_instructions():

    def load_instruction(line):
        ins, val = line.split()
        return ins, int(val)

    with open("input.txt") as file:
        lines = file.read().splitlines()
        instructions = map(lambda x: load_instruction(x), lines)
    
    return list(instructions)


def perform_jmp(pos, acc, val):
    return pos + val, acc

def perform_nop(pos, acc, _):
    return pos + 1, acc

def perform_acc(pos, acc, val):
    return pos + 1, acc + val


def exec_instruction(pos: int, acc: int, executed: Set, change_applied: bool) -> Tuple[int, int]:
    # We found the end!
    if pos >= len(instructions):
        return pos, acc
    
    # Path is an infinite loop
    if pos in executed:
        return -1, -1
    
    executed.add(pos)

    ins, val = instructions[pos]

    if ins == "jmp":
        # Try turning this instruction into a nop
        if not change_applied:
            ppos, pacc = perform_nop(pos, acc, val)
            ppos, pacc = exec_instruction(ppos, pacc, executed.copy(), True)
            if ppos != -1:
                return ppos, pacc
        
        pos, acc = perform_jmp(pos, acc, val)


    elif ins == "acc":
        pos, acc = perform_acc(pos, acc, val)


    else:
        # Try turning this instruction into a jmp
        if not change_applied:
            ppos, pacc = perform_jmp(pos, acc, val)
            ppos, pacc = exec_instruction(ppos, pacc, executed.copy(), True)
            if ppos != -1:
                return ppos, pacc
        
        pos, acc = perform_nop(pos, acc, val)

    return exec_instruction(pos, acc, executed, change_applied)


instructions = load_instructions()
print(exec_instruction(0, 0, set(), False))

