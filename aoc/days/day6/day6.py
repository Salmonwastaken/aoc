from aoc.helpers.lineReader import lineReader
from typing import Union
from copy import deepcopy


def buildArray(content: str) -> list:
    return [list(line) for line in content.splitlines()]


def checkBounds(array: list, x: int, y: int) -> bool:
    return 0 <= x < len(array) and 0 <= y < len(array[0])


def findStart(field: list) -> tuple:
    for number, row in enumerate(field):
        try:
            return (number, row.index("^"))
        except ValueError:
            pass


def traverseField(
    field: list, x: int, y: int, newObstacle: tuple = ()
) -> Union[set, bool]:
    visited = {(x, y)}

    degrees = 0
    originalDegrees = degrees
    originalLocation = (x, y)

    movementHash = {0: (-1, 0), 90: (0, 1), 180: (1, 0), 270: (0, -1)}

    hitObstacles = {}

    while True:
        newX = x + movementHash[degrees][0]
        newY = y + movementHash[degrees][1]
        if not checkBounds(field, newX, newY):
            break

        nextStep = field[newX][newY]

        if nextStep == "#":
            # If newObstacle is not the default empty tuple, eg we passed a valid one and are parsing part 2
            # Ugly >:(, what I get for mishmashing it together
            if newObstacle:
                # Data we need to see if we hit any obstacle for the second time
                originalDegrees = degrees
                originalLocation = (x, y)
                obstacleLocation = (newX, newY)
                tupleKey = (originalDegrees, originalLocation, obstacleLocation)
                # Second run in, we've looped
                if tupleKey in hitObstacles:
                    return True

                hitObstacles[tupleKey] = True

            degrees = (degrees + 90) % 360
            continue
        else:
            x = newX
            y = newY
            visited.add((x, y))

    # very ugly way to mash traversel and loop detection in one
    if not newObstacle:
        return visited
    else:
        return False


def part1(field: list, x: int, y: int) -> int:
    visited = traverseField(field, x, y)

    return len(visited)


def part2(field: list, x: int, y: int) -> int:
    # Get original path
    visited = traverseField(field, x, y)

    # For every place we visited, place an obstacle on that square (except the starting position)
    validObstacles = 0

    for location in visited:
        # We can't put an obstacle on top of the guard
        if location == (x, y):
            print("Skipped initial location")
            continue

        # Copy grid, add blockade to coordinates, traverse again
        newField = deepcopy(field)
        newField[location[0]][location[1]] = "#"
        print(f"Traversing Field for {location}")
        if traverseField(newField, x, y, (location[0], location[1])):
            validObstacles += 1

    return validObstacles


if __name__ == "__main__":
    content = lineReader(False)

    field = buildArray(content)

    start = findStart(field)
    x = start[0]
    y = start[1]

    # p1 = part1(field, x, y)
    # print(f"Part 1: {p1}")
    p2 = part2(field, x, y)
    print(f"Part 2: {p2}")
