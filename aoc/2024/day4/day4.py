from aoc.helpers.lineReader import lineReader

vertical = [(-1, 0), (1, 0)]
horizontal = [(0, -1), (0, 1)]
diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
directions = vertical + horizontal + diagonals


def checkPattern(array: list, x: int, y: int, dx: int, dy: int) -> bool:
    return (
        array[x + dx][y + dy] == "M"
        and array[x + 2 * dx][y + 2 * dy] == "A"
        and array[x + 3 * dx][y + 3 * dy] == "S"
    )


def checkBounds(array: list, x: int, y: int) -> bool:
    return 0 <= x < len(array) and 0 <= y < len(array[0])


def buildArray(content: str) -> list:
    return [list(line) for line in content.splitlines()]


def part1(array: list) -> int:
    xmas = 0

    for x, line in enumerate(array):
        for y, letter in enumerate(line):
            if letter == "X":
                xmas += sum(
                    checkPattern(array, x, y, dx, dy)
                    for dx, dy in directions
                    if all(
                        checkBounds(array, x + dx * i, y + dy * i) for i in range(1, 4)
                    )
                )

    return xmas


def checkPattern2(array: list, x: int, y: int) -> bool:
    valid = ["SAM", "MAS"]

    diagonals = [
        array[x - 1][y - 1] + array[x][y] + array[x + 1][y + 1],
        array[x - 1][y + 1] + array[x][y] + array[x + 1][y - 1],
        array[x + 1][y - 1] + array[x][y] + array[x - 1][y + 1],
        array[x + 1][y + 1] + array[x][y] + array[x - 1][y - 1],
    ]
    return all(diagonal in valid for diagonal in diagonals)


def part2(array: list) -> int:
    xmas = 0

    for x, line in enumerate(array):
        for y, letter in enumerate(line):
            if letter == "A":
                if all(checkBounds(array, x + dx, y + dy) for dx, dy in diagonals):
                    xmas += checkPattern2(array, x, y)

    return xmas


if __name__ == "__main__":
    content = lineReader(False)

    array = buildArray(content)

    p1 = part1(array)
    print(f"Part 1: {p1}")
    p2 = part2(array)
    print(f"Part 2: {p2}")
