from aoc.helpers.lineReader import lineReader
from typing import Union
import cProfile


def containsDigit(lst: list) -> bool:
    for item in lst:
        if isinstance(item, str) and item.isdigit():
            return True
    return False


def getIDs(lst: list) -> list:
    seen = set()
    result = []

    for item in lst:
        if item not in seen and item != ".":
            seen.add(item)
            result.append(item)

    return result


def getTarget(lst: list, target: str) -> list:
    return [index for index, value in enumerate(lst) if value == target]


def findRange(lst: list, target: str, start: int = None) -> tuple:
    if target not in lst:
        exit()

    if start is None:
        # If no start is defined, we find the first one
        start = lst.index(target)

    i = 0
    while start + i < len(lst) and lst[start + i] == target:
        i += 1

    end = start + i

    return (start, end)


# Build a list like in the example
# if blocks = False
# 12345 -> 0..111....22222
def buildBlock(content: str) -> list:
    file = True
    blockID = 0
    output = []

    for i in content:
        # Don't need empty strings, do want to swap
        if i == "0":
            file = not file
            continue

        if file:
            output.extend([f"{blockID}"] * int(i))
            blockID += 1
        else:
            output.extend(["."] * int(i))

        # True becomes False, False becomes True
        file = not file

    return output


# Compact it
# 0..111....22222 -> 022111222......
def compactBlock(output: list) -> list:
    for key, val in enumerate(reversed(output)):
        newPlace = output.index(".")
        oldPlace = -key - 1
        # Check if there's any numbers remaining
        if not containsDigit(output[newPlace:]):
            break

        # Swap
        output[newPlace], output[oldPlace] = output[oldPlace], output[newPlace]

    return output


# This time, attempt to move whole files to the leftmost span of free space blocks that could fit the file.
# Attempt to move each file exactly once in order of decreasing file ID number starting with the file with the highest file ID number.
# If there is no span of free space to the left of a file that is large enough to fit the file, the file does not move.
def altCompact(output: list) -> list:
    numbers = list(reversed(getIDs(output)))

    free_ranges = []
    i = 0
    # CBA to use my findRange for this as well
    while i < len(output):
        if output[i] == ".":
            start = i
            while i < len(output) and output[i] == ".":
                i += 1
            free_ranges.append((start, i))
        else:
            i += 1

    for number in numbers:
        # print(number)
        oldStart, oldEnd = findRange(output, number)
        numberLength = oldEnd - oldStart

        for key, value in enumerate(free_ranges):
            newStart, newEnd = value
            dotLength = newEnd - newStart

            if dotLength >= numberLength and newStart < oldStart:
                # Update available ranges
                start = free_ranges[key][0] + numberLength
                if start == newEnd:
                    del free_ranges[key]
                else:
                    # Adjust start
                    free_ranges[key] = (start, newEnd)

                output[newStart : newStart + numberLength] = output[oldStart:oldEnd]
                output[oldStart:oldEnd] = ["."] * numberLength
                break

    return output


def calculateChecksum(compacted: Union[str, list]) -> int:
    total = 0
    for k, v in enumerate(compacted):
        if v == ".":
            continue
        total += k * int(v)

    return total


def part1(content: str) -> int:
    output = buildBlock(content)
    compacted = compactBlock(output)

    total = calculateChecksum(compacted)

    return total


def part2(content: str) -> int:
    output = buildBlock(content)
    compacted = altCompact(output)

    total = calculateChecksum(compacted)

    return total


if __name__ == "__main__":
    content = lineReader(False)

    # p1 = part1(content)
    # print(f"Part 1: {p1}")
    p2 = part2(content)
    print(f"Part 2: {p2}")
