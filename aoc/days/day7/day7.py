from aoc.helpers.lineReader import lineReader

# Operators are always evaluated left-to-right, not according to precedence rules!
OPERATORS = ["+", "*"]


def isValid(result, rest):
    if len(rest) == 1:
        return rest[0] == result

    last = rest[-1]

    if result % last == 0:
        possible_mul = isValid(result // last, rest[:-1])
    else:
        possible_mul = False

    possible_add = isValid(result - last, rest[:-1])
    return possible_mul or possible_add


def part1(content):
    total = 0

    for line in content:
        split = line.split(":")
        value = int(split[0])
        numbers = [int(n) for n in split[1].lstrip().split()]
        if isValid(value, numbers):
            total += value

    return total


if __name__ == "__main__":
    content = lineReader()

    p1 = part1(content)
    print(f"Part 1: {p1}")
