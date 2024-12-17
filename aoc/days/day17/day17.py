from aoc.helpers.lineReader import lineReader
import re


# opcode 0
# writes A
def adv(value, combo):
    operand = pow(2, combo)
    return int(value / operand)


# opcode 1
# writes B
def bxl(value, literal):
    return value ^ literal


# opcode 2
# writes B
def bst(combo):
    return combo % 8


# opcode 3
# writes instruction pointer
# if applied, does not trigger default increase
def jnz(register_a, literal, instruction_pointer):
    if register_a == 0:
        return instruction_pointer + 2
    else:
        return literal


# opcode 4
# writes B
def bxc(register_b, register_c):
    return register_b ^ register_c


# opcode 5
# writes output
def out(combo):
    return combo % 8


# 6 and 7 do exactly the same as 0, but write to a different register.


content = lineReader()

digits = re.compile(r"\d+")
numbers = []

for line in content:
    digit = re.findall(digits, line)
    if digit != []:
        numbers.append(digit)

register_a = int(numbers[0][0])
register_b = int(numbers[1][0])
register_c = int(numbers[2][0])

instructions = [int(i) for i in numbers[3]]

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

output = []

print(
    f"Register A: {register_a}\nRegister B: {register_b}\nRegister C: {register_c}\nOutput: {",".join(output)}\n"
)

instruction_pointer = 0

while instruction_pointer < len(instructions):
    opcode = instructions[instruction_pointer]
    operand = instructions[instruction_pointer + 1]

    match opcode:
        case 0:
            register_a = adv(register_a, combo_map[operand]())
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
            output.append(str(new))
            instruction_pointer += 2
        case 6:
            register_b = adv(register_a, combo_map[operand]())
            instruction_pointer += 2
        case 7:
            register_c = adv(register_a, combo_map[operand]())
            instruction_pointer += 2

print(
    f"Register A: {register_a}\nRegister B: {register_b}\nRegister C: {register_c}\nOutput: {",".join(output)}\n"
)
