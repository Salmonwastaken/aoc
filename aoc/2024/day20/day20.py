from aoc.helpers.lineReader import lineReader
from aoc.helpers.grid_helpers import find_index, build_array
from collections import deque, defaultdict
from bisect import bisect_left

inf = float("inf")


def dist(pos1, pos2):
    r1, c1 = pos1
    r2, c2 = pos2
    return abs(r1 - r2) + abs(c1 - c2)


def get_distances(field, finish):
    distances = defaultdict(lambda: inf)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(finish, 0)])
    visited = set()

    while queue:
        finish, distance = queue.popleft()

        if finish in visited:
            continue
        visited.add(finish)
        distances[finish] = distance
        x, y = finish
        for dx, dy in dirs:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) not in visited and field[new_x][new_y] != "#":
                queue.append([(new_x, new_y), distance + 1])

    return distances


def cheating_paths(distances, threshold, cheat_duration=2):
    total_saved = defaultdict(int)
    distance_list = [(d, pos) for pos, d in distances.items()]
    distance_list.sort
    n = len(distance_list)
    for i in range(n):
        d1, pos1 = distance_list[i]
        j = bisect_left(distance_list, (d1 + threshold - 1, (-1, -1)))
        for k in range(j, n):
            d2, pos2 = distance_list[k]
            if dist(pos1, pos2) > cheat_duration:
                continue
            saved = (d2 - d1) - dist(pos1, pos2)
            if saved >= threshold:
                total_saved[saved] += 1

    return sum(total_saved.values())


content = lineReader()

field = build_array(content)

finish = find_index(field, "E")[0]

distances = get_distances(field, finish)
# Part 1
print(cheating_paths(distances, 100))
# Part 2
print(cheating_paths(distances, 100, 20))
