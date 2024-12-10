from aoc.helpers.lineReader import lineReader


vertical = [(-1, 0), (1, 0)]
horizontal = [(0, -1), (0, 1)]
DIRECTIONS = vertical + horizontal


def buildArray(content: str) -> list:
    return [list(line) for line in content]


def checkBounds(array: list, x: int, y: int) -> bool:
    return 0 <= x < len(array) and 0 <= y < len(array[0])


def findStarts(array: list) -> list:
    starts = []
    for x, line in enumerate(array):
        for y, value in enumerate(line):
            if value == "0":
                starts.append((x, y))

    return starts


def isValid(array: list, x: int, y: int, path, expectedNumber: str) -> bool:
    return (
        checkBounds(array, x, y)
        and (x, y) not in path
        and array[x][y] == str(expectedNumber)
    )


def dfs(grid, startX, startY, once=True):
    all_paths = set()
    stack = [(startX, startY, [(startX, startY)], 0)]

    while stack:
        x, y, path, current_digit = stack.pop()

        if current_digit == 9 and grid[x][y] == "9":
            if once:
                # How many 9s can we reach? (part1)
                all_paths.add((x, y))
            else:
                # All possible paths to all 9s (part2)
                all_paths.add(tuple(path))
            continue

        for dx, dy in DIRECTIONS:
            next_x, next_y = x + dx, y + dy

            if isValid(grid, next_x, next_y, path, current_digit + 1):
                stack.append(
                    (next_x, next_y, path + [(next_x, next_y)], current_digit + 1)
                )

    return all_paths


if __name__ == "__main__":
    content = lineReader()

    field = buildArray(content)
    startLocations = findStarts(field)

    p1 = 0

    for x, y in startLocations:
        paths1 = dfs(field, x, y)
        p1 += len(paths1)
    print(p1)

    p2 = 0

    for x, y in startLocations:
        paths2 = dfs(field, x, y, False)
        p2 += len(paths2)

    print(p2)
