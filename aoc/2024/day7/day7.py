from aoc.helpers.lineReader import lineReader
from itertools import product


def test(combo, numbers):
    ans = numbers[0]
    for i in range(1, len(numbers)):
        if combo[i - 1] == "+":
            ans += numbers[i]
        elif combo[i - 1] == "|":
            ans = int(f"{ans}{numbers[i]}")
        else:
            ans *= numbers[i]
    return ans


def run(lines, ops):
    total = 0

    for i, line in enumerate(lines):
        parts = line.split()
        value = int(parts[0][:-1])
        numbers = list(map(int, parts[1:]))

        for combo in product(ops, repeat=len(numbers) - 1):
            if test(combo, numbers) == value:
                total += value
                break

    return total


if __name__ == "__main__":
    content = lineReader()

    p1 = run(content, "+*")
    print(f"Part 1: {p1}")
    p2 = run(content, "+*|")
    print(f"Part 2: {p2}")
