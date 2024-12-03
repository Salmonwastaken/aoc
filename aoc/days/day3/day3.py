from aoc.helpers.lineReader import lineReader

import re


def parseInstructions(c):
    pat = re.compile(pattern=r"mul\((\d{1,3}),(\d{1,3})\)")
    total = 0

    matches = re.finditer(pat, c)
    for match in matches:
        total += int(match.group(1)) * int(match.group(2))

    return total


def part1(content):
    return parseInstructions(content)


def part2(content):
    patternDo = re.compile(r"do\(\)(.*?)(?:don't\(\)|$)", re.DOTALL)

    enabledRange = []

    # Find the first don't
    dont = content.find("don't()")
    # Capture everything from do till don't or end of file (ignoring line endings)
    do = patternDo.findall(content)

    # Capture everything from the start till that first don't
    enabledRange.append(content[0:dont])
    enabledRange += do

    # Turn list of strings into one big happy string
    stringedRange = "".join(enabledRange)

    return parseInstructions(stringedRange)


if __name__ == "__main__":
    content = lineReader(False)

    p1 = part1(content)
    print(f"Part 1: {p1}")
    p2 = part2(content)
    print(f"Part 2: {p2}")
