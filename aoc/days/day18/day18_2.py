from aoc.helpers.lineReader import lineReader
from heapq import heappush, heappop
import os
import time

# Define color codes
RED = "\033[91m"  # Red
GREY = "\033[90m"  # Grey
GREEN = "\033[92m"  # Green
PURPLE = "\033[95m"  # Purple
RESET = "\033[0m"  # Reset color


# Visual Debug Stuff
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def print_path(field, path=[]):
    # Temporarily mark path
    for step in path:
        x, y = step
        field[x][y] = "O"

    # Print the field with colors
    for line in field:
        colored_line = ""
        for cell in line:
            # Assigning colors to the cells
            if cell == "#":
                colored_line += RED + "#" + RESET
            elif cell == ".":
                colored_line += GREY + "." + RESET
            elif cell == "O":
                colored_line += GREEN + "O" + RESET
            elif cell == "X":
                colored_line += PURPLE + "X" + RESET
            else:
                colored_line += cell
        print(colored_line)

    # Reset the path and print it again after finishing
    for step in path:
        x, y = step
        field[x][y] = "."

    print()  # Extra line break after printing the field for readability


# Actual checks
def check_bounds(array, x, y):
    return 0 <= x < len(array) and 0 <= y < len(array[0])


def is_valid(array, x, y, visited):
    return check_bounds(array, x, y) and (x, y) not in visited and array[x][y] != "#"


def a_star(field, cost, start_x, start_y, finish_x, finish_y):
    pq = []
    heappush(pq, (0, 0, start_x, start_y, [(start_x, start_y)]))

    visited = set()
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    def heuristic(x, y):
        # Manhattan distance
        return abs(x - finish_x) + abs(y - finish_y)

    while pq:
        f, g, x, y, path = heappop(pq)

        if (x, y) == (finish_x, finish_y):
            return True, path

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in dirs:
            new_x, new_y = x + dx, y + dy

            if is_valid(field, new_x, new_y, visited):
                new_g = g + cost[new_x][new_y]  # Cost to next neighbor
                new_f = new_g + heuristic(new_x, new_y)  # Total cost
                heappush(pq, (new_f, new_g, new_x, new_y, path + [(new_x, new_y)]))

    return False, path


content = lineReader()
X_LEN = 71 if len(content) > 1000 else 7
Y_LEN = 71 if len(content) > 1000 else 7
BYTES = 1024 if len(content) > 1000 else 12

blockades = [(int(x), int(y)) for entry in content for x, y in [entry.split(",")]]
field = []
cost = []

for y in range(Y_LEN):
    field.append([])
    cost.append([])
    for x in range(X_LEN):
        if (x, y) in blockades[:BYTES]:
            field[y].append("#")
            cost[y].append(float("inf"))
        else:
            field[y].append(".")
            cost[y].append(1)

i = 1024 if len(content) > 1000 else 12
last_path = []
# Let's just bruteforce it
while True:
    block_x, block_y = blockades[i]
    field[block_y][block_x] = "#"
    possible, shortest_path = a_star(field, cost, 0, 0, X_LEN - 1, Y_LEN - 1)

    if last_path != shortest_path:
        clear_console()
        print_path(field, shortest_path)
        time.sleep(0.1)
        last_path = shortest_path

    if not possible:
        field[block_y][block_x] = "X"
        clear_console()
        print_path(field, shortest_path)
        break

    i += 1

print(blockades[i])
