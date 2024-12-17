from aoc.helpers.lineReader import lineReader
import re
from collections import deque


# opcode 0
# writes A
def adv(value, combo, opcode):
    operand = pow(2, combo)
    result = int(value / operand)
    return result


# opcode 1
# writes B
def bxl(value, literal):
    result = value ^ literal
    return result


# opcode 2
# writes B
def bst(combo):
    result = combo % 8
    return result


# opcode 3
# writes instruction pointer
# if applied, does not trigger default increase
def jnz(register_a, literal, instruction_pointer):
    if register_a == 0:
        result = instruction_pointer + 2
    else:
        result = literal
    return result


# opcode 4
# writes B
def bxc(register_b, register_c):
    result = register_b ^ register_c
    return result


# opcode 5
# writes output
def out(combo):
    result = combo % 8
    return result


# 6 and 7 do exactly the same as 0, but write to a different register.


def program(register_a, register_b, register_c, instructions):
    # All combos are functions that either return the current value of a register or simply their literal value
    combo_map = {
        0: lambda: 0,
        1: lambda: 1,
        2: lambda: 2,
        3: lambda: 3,
        4: lambda: register_a,
        5: lambda: register_b,
        6: lambda: register_c,
        7: "RESERVED",
    }
    instruction_pointer = 0
    output = []

    # print(
    #     f"Register A: {register_a}\nRegister B: {register_b}\nRegister C: {register_c}\nOutput: {",".join(map(str, output))}\n"
    # )

    while instruction_pointer < len(instructions):
        opcode = instructions[instruction_pointer]
        operand = instructions[instruction_pointer + 1]
        match opcode:
            case 0:
                register_a = adv(register_a, combo_map[operand](), opcode)
                instruction_pointer += 2
            case 1:
                register_b = bxl(register_b, operand)
                instruction_pointer += 2
            case 2:
                register_b = bst(combo_map[operand]())
                instruction_pointer += 2
            case 3:
                instruction_pointer = jnz(register_a, operand, instruction_pointer)
            case 4:
                register_b = bxc(register_b, register_c)
                instruction_pointer += 2
            case 5:
                new = out(combo_map[operand]())
                output.append(new)
                instruction_pointer += 2
            case 6:
                register_b = adv(register_a, combo_map[operand](), opcode)
                instruction_pointer += 2
            case 7:
                register_c = adv(register_a, combo_map[operand](), opcode)
                instruction_pointer += 2
    # print(
    #     f"Register A: {register_a}\nRegister B: {register_b}\nRegister C: {register_c}\nOutput: {",".join(map(str, output))}\n"
    # )
    return output


def decompiled(instructions):
    candidates = deque([0])

    min_candidate = 2 ** (3 * (len(instructions) - 1))

    while candidates and candidates[-1] < min_candidate:
        seed = candidates.popleft()
        for a in range(2**6):
            a += seed * 64
            out = program(
                register_a=a, register_b=0, register_c=0, instructions=instructions
            )
            if a < 8:
                out.insert(0, 0)
            if out == instructions[-(len(out)) :]:
                candidates.append(a)
            if out == instructions:
                break

    # Return lowest possible input
    return candidates.pop()


content = lineReader(False)

digits = re.compile(r"\d+")
numbers = []

a, b, c, *instructions = (int(i) for i in re.findall(digits, content))
print(instructions)

p2 = decompiled(instructions)
print(p2)
