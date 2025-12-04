from aoc.helpers.lineReader import lineReader
from aoc.helpers.grid_helpers import build_array, find_index
import time

s = time.perf_counter()
content = lineReader()
grid = build_array(content)
rolls = find_index(grid, "@")

vertical = [(-1, 0), (1, 0)]
horizontal = [(0, -1), (0, 1)]
diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
directions = vertical + horizontal + diagonals
print(f"Shared prep took: {(time.perf_counter() - s):.6f}s\n")

s = time.perf_counter()
# Part 1
answer = 0
roll_set = set(rolls)
for rx, ry in rolls:
    surrounding_locations = []

    # Determine all surrounding locations
    surrounding_locations = [(rx - dx, ry - dy) for dx, dy in directions]

    # Compare amount of surrounding locations with known locations of rolls
    matches = len(roll_set.intersection(surrounding_locations))

    if matches < 4:
        answer += 1

print(f"Part 1: {answer}")
print(f"Part 1 took: {(time.perf_counter() - s):.6f}s\n")

s = time.perf_counter()
# Part 2
answer = 0
removed = 999
while removed != 0:
    removed = 0
    roll_set = set(rolls)

    for pos, roll in enumerate(rolls):
        rx, ry = roll
        surrounding_locations = []

        # Determine all surrounding locations
        surrounding_locations = [(rx - dx, ry - dy) for dx, dy in directions]

        # Compare amount of surrounding locations with known locations of rolls
        matches = len(roll_set.intersection(surrounding_locations))

        if matches < 4:
            removed += 1
            # Remove rolls from the original list, to be used on the next iteration of the while loop
            # While we continue to use the roll_set to determine which rolls to remove on the current iteration
            rolls.pop(pos)

    answer += removed

print(f"Part 2: {answer}")
print(f"Part 2 took: {(time.perf_counter() - s):.6f}s")
print()
