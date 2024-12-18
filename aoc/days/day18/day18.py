from aoc.helpers.lineReader import lineReader
from heapq import heappush, heappop
import time
import math
import os


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


def a_star(field, cost, start_x, start_y, finish_x, finish_y):
    pq = []
    heappush(pq, (0, 0, start_x, start_y, []))

    visited = set()
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    def heuristic(x, y):
        # Manhattan distance
        return abs(x - finish_x) + abs(y - finish_y)

    while pq:
        f, g, x, y, path = heappop(pq)

        clear_console()
        print_path(field, path + [(x, y)])
        time.sleep(0.01)

        if (x, y) == (finish_x, finish_y):
            return path

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in dirs:
            new_x, new_y = x + dx, y + dy

            if is_valid(field, new_x, new_y, visited):
                new_g = g + cost[new_x][new_y]  # Cost to next neighbor
                new_f = new_g + heuristic(new_x, new_y)  # Total cost
                heappush(pq, (new_f, new_g, new_x, new_y, path + [(new_x, new_y)]))

    return None


X_LEN = 71
Y_LEN = 71
BYTES = 1024

content = lineReader()

blockades = [
    (int(x), int(y)) for entry in content[:BYTES] for x, y in [entry.split(",")]
]
print(blockades)
field = []
cost = []

for y in range(Y_LEN):
    field.append([])
    cost.append([])
    for x in range(X_LEN):
        if (x, y) in blockades:
            field[y].append("#")
            cost[y].append(float("inf"))
        else:
            field[y].append(".")
            cost[y].append(1)


print_path(field)
shortest_path = a_star(field, cost, 0, 0, X_LEN - 1, Y_LEN - 1)
print_path(field, shortest_path)

print(shortest_path)
print(len(shortest_path))
