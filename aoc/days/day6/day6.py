from aoc.helpers.lineReader import lineReader
from collections import defaultdict
from copy import deepcopy
from typing import Union


# Build the field grid from the input content
def buildArray(content: str) -> list:
    return [list(line) for line in content.splitlines()]


# Check if the coordinates are within bounds
def checkBounds(array: list, x: int, y: int) -> bool:
    return 0 <= x < len(array) and 0 <= y < len(array[0])


# Find the starting position marked by '^'
def findStart(field: list) -> tuple:
    for number, row in enumerate(field):
        try:
            return (number, row.index("^"))
        except ValueError:
            pass


# Traverse the field while checking for obstacles and loop detection
def traverseField(
    field: list, x: int, y: int, newObstacle: tuple = ()
) -> Union[set, bool]:
    visited = {(x, y)}

    degrees = 0
    movementHash = {0: (-1, 0), 90: (0, 1), 180: (1, 0), 270: (0, -1)}

    hitObstacles = defaultdict(bool)

    while True:
        newX, newY = x + movementHash[degrees][0], y + movementHash[degrees][1]

        if not checkBounds(field, newX, newY):
            break

        nextStep = field[newX][newY]

        if nextStep == "#":
            if newObstacle:
                obstacleLocation = (newX, newY)
                tupleKey = (degrees, (x, y), obstacleLocation)
                if hitObstacles[tupleKey]:  # We hit the obstacle again
                    return True

                hitObstacles[tupleKey] = True

            degrees = (degrees + 90) % 360
            continue
        else:
            x, y = newX, newY
            visited.add((x, y))

    return visited if not newObstacle else False


# Part 1: Traverse the field and return the number of visited locations
def part1(field: list, x: int, y: int) -> int:
    visited = traverseField(field, x, y)
    return len(visited)


# Part 2: Count valid obstacles that block the path without causing loops
def part2(field: list, x: int, y: int) -> int:
    visited = traverseField(field, x, y)
    validObstacles = 0

    for location in visited:
        if location == (x, y):
            continue  # Skip the initial location

        # Create a new field with the obstacle at the current location
        newField = deepcopy(field)
        newField[location[0]][location[1]] = "#"

        if traverseField(newField, x, y, (location[0], location[1])):
            validObstacles += 1

    return validObstacles


if __name__ == "__main__":
    content = lineReader(False)
    field = buildArray(content)
    start = findStart(field)
    x, y = start[0], start[1]

    p1 = part1(field, x, y)
    print(f"Part 1: {p1}")
    p2 = part2(field, x, y)
    print(f"Part 2: {p2}")
