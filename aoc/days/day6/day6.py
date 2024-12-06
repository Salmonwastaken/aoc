from aoc.helpers.lineReader import lineReader
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
        if "^" in row:
            return (number, row.index("^"))
    return None


# Directions: (UP, RIGHT, DOWN, LEFT)
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def traverseField(
    field: list, x: int, y: int, checkForLoop: bool = False
) -> Union[set, bool]:
    visited = {(x, y)}
    direction = 0
    visitedObstacles = set()

    while True:
        dx, dy = DIRECTIONS[direction]
        newX, newY = x + dx, y + dy

        if not checkBounds(field, newX, newY):
            break

        nextStep = field[newX][newY]

        if nextStep == "#":
            if checkForLoop:
                obstacleLocation = (newX, newY)
                stateKey = (direction, (x, y), obstacleLocation)
                # Unique key already exists, so we've hit it a second time
                # This means we're looping!
                if stateKey in visitedObstacles:
                    return True

                visitedObstacles.add(stateKey)

            # Turn 90 degrees clockwise
            direction = (direction + 1) % 4
            continue
        else:
            x, y = newX, newY
            visited.add((x, y))

    return visited if not checkForLoop else False


def part1(field: list, x: int, y: int) -> int:
    visited = traverseField(field, x, y)
    return len(visited)


def part2(field: list, x: int, y: int) -> int:
    visited = traverseField(field, x, y)
    validObstacles = 0

    for location in visited:
        if location == (x, y):
            continue

        # Temporarily block the location
        field[location[0]][location[1]] = "#"

        # Check if whether the new path generates a loop
        if traverseField(field, x, y, checkForLoop=True):
            validObstacles += 1

        # Revert the field to the original state
        field[location[0]][location[1]] = "."

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
