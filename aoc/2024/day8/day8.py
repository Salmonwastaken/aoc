from aoc.helpers.lineReader import lineReader
from collections import defaultdict


def buildArray(content: str) -> list:
    return [list(line) for line in content]


def checkBounds(array: list, x: int, y: int) -> bool:
    return 0 <= x < len(array) and 0 <= y < len(array[0])


def parseInput(field: list) -> dict:
    antennas = defaultdict(list)

    # Build a list of: antenna type and their locations
    for x, line in enumerate(field):
        for y, value in enumerate(line):
            if value == ".":
                continue

            antennas[value].append((x, y))

    return antennas


def calculateAntinodes(field: list, antennas: dict, propagate: bool = False) -> int:
    antinodes = set()

    # Loop through antennas and mark spawned antinodes
    for antenna, locations in antennas.items():
        # No possible antinodes, idk if it even occurs.
        if len(locations) <= 1:
            pass

        # Check the distance between every location for every location
        for startX, startY in locations:
            for locationX, locationY in locations:
                xDiff, yDiff = startX - locationX, startY - locationY
                # # Same location, so we can skip
                if xDiff == 0 and yDiff == 0:
                    if propagate:
                        antinodes.add((startX, startY))
                    continue

                newX, newY = startX + xDiff, startY + yDiff

                # Now we add em all
                while checkBounds(field, newX, newY):
                    antinodes.add((newX, newY))
                    if not propagate:
                        break
                    newX += xDiff
                    newY += yDiff

    return len(antinodes)


if __name__ == "__main__":
    content = lineReader()

    field = buildArray(content)

    antennas = parseInput(field)

    anti1 = calculateAntinodes(field, antennas)
    print(anti1)
    anti2 = calculateAntinodes(field, antennas, True)
    print(anti2)
