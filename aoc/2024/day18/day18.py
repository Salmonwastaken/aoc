from aoc.helpers.lineReader import lineReader
from collections import deque
import os
import time


# Visual Debug stuff
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def print_path(field, path=[]):
    for step in path:
        x, y = step
        field[x][y] = "O"

    # Print the field
    for line in field:
        print("".join(line))

    # Reset the field to its original state
    for step in path:
        x, y = step
        field[x][y] = "."
    print()


# Actual checks
def check_bounds(array, x, y):
    return 0 <= x < len(array) and 0 <= y < len(array[0])


def is_valid(array, x, y, visited):
    return check_bounds(array, x, y) and (x, y) not in visited and array[x][y] != "#"


def bfs(field, start_x, start_y, finish_x, finish_y):
    queue = deque([(start_x, start_y, [])])

    visited = set()
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    while queue:
        x, y, path = queue.popleft()

        if (x, y) == (finish_x, finish_y):
            return path

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in dirs:
            new_x, new_y = x + dx, y + dy

            if is_valid(field, new_x, new_y, visited):
                queue.append((new_x, new_y, path + [(new_x, new_y)]))

    return None


content = lineReader()

X_LEN = 71 if len(content) > 1000 else 7
Y_LEN = 71 if len(content) > 1000 else 7
BYTES = 1024 if len(content) > 1000 else 12

blockades = [
    (int(x), int(y)) for entry in content[:BYTES] for x, y in [entry.split(",")]
]
field = []
cost = []

for y in range(Y_LEN):
    field.append([])
    for x in range(X_LEN):
        if (x, y) in blockades:
            field[y].append("#")
        else:
            field[y].append(".")

# print_path(field)
shortest_path = bfs(field, 0, 0, X_LEN - 1, Y_LEN - 1)
# print_path(field, shortest_path)

print(len(shortest_path))
