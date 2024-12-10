from aoc.helpers.lineReader import lineReader


def containsDigit(lst: list) -> bool:
    return any(item.isdigit() for item in lst if isinstance(item, str))


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


def findNumberRange(lst: list, target: str, start: int = 0) -> tuple:
    while start < len(lst) and lst[start] != target:
        start += 1
    if start == len(lst):
        raise ValueError(f"Target '{target}' not found in the list.")

    end = start
    while end < len(lst) and lst[end] == target:
        end += 1

    return (start, end)


def findFreeRanges(output: list) -> list:
    free_ranges = []
    i = 0
    while i < len(output):
        if output[i] == ".":
            start = i
            while i < len(output) and output[i] == ".":
                i += 1
            free_ranges.append((start, i))
        else:
            i += 1
    return free_ranges


# Build a list like in the example
# 2333133121414131402 -> 00...111...2...333.44.5555.6666.777.888899
def buildBlock(content: str) -> list:
    file = True
    blockID = 0
    output = []

    for char in content:
        count = int(char)
        if count == 0:
            file = not file
            continue

        fill = f"{blockID}" if file else "."
        output.extend([fill] * count)
        if file:
            blockID += 1
        file = not file
    return output


# Compact it
# 00...111...2...333.44.5555.6666.777.888899 -> 0099811188827773336446555566..............
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


# Alternative compact (for  part 2)
# 00...111...2...333.44.5555.6666.777.888899 -> 00992111777.44.333....5555.6666.....8888..
def altCompact(output: list) -> list:
    numbers = reversed(getIDs(output))
    free_ranges = findFreeRanges(output)

    for number in numbers:
        oldStart, oldEnd = findNumberRange(output, number)
        numberLength = oldEnd - oldStart

        for i, (newStart, newEnd) in enumerate(free_ranges):
            if newEnd - newStart >= numberLength and newStart < oldStart:
                # Move the file
                output[newStart : newStart + numberLength] = output[oldStart:oldEnd]
                output[oldStart:oldEnd] = ["."] * numberLength

                # Update free ranges
                free_ranges[i] = (newStart + numberLength, newEnd)
                if free_ranges[i][0] == free_ranges[i][1]:
                    free_ranges.pop(i)
                break
    return output


def calculateChecksum(compacted: list) -> int:
    return sum(k * int(v) for k, v in enumerate(compacted) if v != ".")


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

    p1 = part1(content)
    print(f"Part 1: {p1}")
    p2 = part2(content)
    print(f"Part 2: {p2}")
