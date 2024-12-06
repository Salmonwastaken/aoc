from aoc.helpers.lineReader import lineReader


def buildArray(content: str) -> list:
    return [list(line) for line in content.splitlines()]


def checkBounds(array: list, x: int, y: int) -> bool:
    return 0 <= x < len(array) and 0 <= y < len(array[0])


if __name__ == "__main__":
    content = lineReader(False)

    field = buildArray(content)

    for number, row in enumerate(field):
        try:
            start = (number, row.index("^"))
        except ValueError:
            pass

    x = start[0]
    y = start[1]

    visited = {(x, y)}

    degrees = 0

    movementHash = {0: (-1, 0), 90: (0, 1), 180: (1, 0), 270: (0, -1)}

    while True:
        print(visited)
        newX = x + movementHash[degrees][0]
        newY = y + movementHash[degrees][1]
        if not checkBounds(field, newX, newY):
            break
        nextStep = field[newX][newY]
        if nextStep == "#":
            print("Invalid Location found!")
            degrees = (degrees + 90) % 360
            continue
        else:
            print("Valid Location found!")
            x = newX
            y = newY
            visited.add((x, y))

    print(len(visited))
