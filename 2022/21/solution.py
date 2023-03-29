#!/usr/bin/env python3
import operator
from collections.abc import Callable
from dataclasses import dataclass
from operator import add, sub, mul, floordiv

BinOp = Callable[[int, int], int]
Instruction = int | str | tuple[str, BinOp, str]

operators: dict[str, BinOp] = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": floordiv,
}

op_symbol: dict[BinOp, str] = {
    add:      "+",
    sub:      "-",
    mul:      "*",
    floordiv: "/",
}

@dataclass
class Monkehs:
    instructions: dict[str, Instruction]

    def eval(self, name) -> int | str | list:
        match self.instructions[name]:
            case [lvalue, op, rvalue]:
                return self._eval_instruction_abstraction((self.eval(lvalue), op, self.eval(rvalue)))
            case number:
                return number

    def _eval_instruction_abstraction(self, instruction_abstraction):
        match instruction_abstraction:
            case [int(lvalue), op, int(rvalue)]:
                return op(lvalue, rvalue)
            case [str(lvar), op, int(rvalue)]:
                return [(op, rvalue)]
            case [int(lvalue), op, str(rvar)]:
                return [(lvalue, op)]
            case [list(calculation), op, int(rvalue)]:
                calculation.append((op, rvalue))
                return calculation
            case [int(lvalue), op, list(calculation)]:
                calculation.append((lvalue, op))
                return calculation
            case what:
                print(what)
                assert False, "You suck"

def parse(line: str) -> tuple[str, Instruction]:
    match line.split():
        case [name, number]:
            return name[:-1], int(number)
        case [name, name_a, op, name_b]:
            return name[:-1], (name_a, operators[op], name_b)
        case _:
            assert False, "You suck"

def main(name) -> None:
    with open("input.txt") as f:
        lines = [parse(line) for line in f.read().splitlines()]
    m = Monkehs(dict(lines))
    print(m.eval(name))

reverse_op = {
    add:      sub,
    sub:      add,
    mul:      floordiv,
    floordiv: mul,
}

def main2() -> None:
    with open("input.txt") as f:
        lines = [parse(line) for line in f.read().splitlines()]
    m = Monkehs(dict(lines))

    m.instructions["humn"] = "x"
    calculation = m.eval('qntq')
    eq_value = m.eval('qgth')
    for operation_instruction in reversed(calculation):
        match operation_instruction:
            case [op, int(rvalue)]:
                eq_value = reverse_op[op](eq_value, rvalue)
            case [int(lvalue), operator.sub | operator.floordiv as op]:
                eq_value = op(lvalue, eq_value)
            case [int(lvalue), op]:
                eq_value = reverse_op[op](eq_value, lvalue)
    print(eq_value)
    m.instructions["humn"] = eq_value
    assert m.eval('qntq') == m.eval('qgth')

if __name__ == "__main__":
    main("root")
    main2()
