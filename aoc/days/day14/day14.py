from aoc.helpers.lineReader import lineReader
import re
from math import prod


def findMiddle(i) -> int:
    return i // 2


def wrap(x, y, total_x, total_y):
    new_x = x % total_x
    new_y = y % total_y
    return new_x, new_y


def find_quadrant(x, y, x_mid, y_mid):
    if x < x_mid and y < y_mid:  # Top-left
        return 1
    elif x < x_mid and y > y_mid:  # Top-Right
        return 2
    elif x > x_mid and y < y_mid:  # Bottom-Left
        return 3
    elif x > x_mid and y > y_mid:  # Bottom-right
        return 4


if __name__ == "__main__":
    content = lineReader()

    cords_re = re.compile(r"-?\d+")

    total_x, total_y = 103, 101
    seconds = 100
    field = [[0] * total_y for _ in range(total_x)]

    x_mid = findMiddle(total_x)
    y_mid = findMiddle(total_y)

    field[x_mid] = [" "] * total_y
    for key, _ in enumerate(field):
        field[key][y_mid] = " "

    quadrants = {1: 0, 2: 0, 3: 0, 4: 0}

    positions = []

    for robot in content:
        (start_y, start_x, movement_y, movement_x) = [
            int(i) for i in re.findall(cords_re, robot)
        ]

        total_movement_x = movement_x * seconds
        total_movement_y = movement_y * seconds

        final_x = start_x + total_movement_x
        final_y = start_y + total_movement_y

        x, y = wrap(final_x, final_y, total_x, total_y)

        if x == x_mid or y == y_mid:
            continue

        field[x][y] += 1

        quadrant = find_quadrant(x, y, x_mid, y_mid)
        quadrants[quadrant] += 1

    for line in field:
        for c in line:
            print(c, end=" ")
        print()

    total = prod(quadrants.values())
    print(total)
