#!/usr/bin/env python3

def execute(code):
    seen = set()
    acc = 0
    i = 0

    while True:
        op, arg = code[i]
        seen.add(i)
        if op == "jmp":
            i += arg
        elif op == "acc":
            i += 1
            acc += arg
        else:
            i += 1

        if i in seen:
            return False, acc
        if i >= len(code):
            return True, acc

def attempt_repair(code, i):
    if code[i][0] == "jmp":
        code[i][0] = "nop"
        retval = execute(code)
        code[i][0] = "jmp"
        return retval
    elif code[i][0] == "nop":
        code[i][0] = "jmp"
        retval = execute(code)
        code[i][0] = "nop"
        return retval
    return False, 0

with open("input.txt") as f:
    code = f.read().splitlines()
    code = (line.split() for line in code)
    code = [[op, int(arg)] for op, arg in code]

print(execute(code)[1])
repair_attempts = (attempt_repair(code, i) for i in range(len(code)))
print(next(acc for success, acc in repair_attempts if success))
