from aoc.helpers.lineReader import lineReader
from collections import deque


def build_array(content):
    return [list(line) for line in content]


def find_race(field):
    for x, line in enumerate(field):
        for y, value in enumerate(line):
            if value == "S":
                start = (x, y)
            if value == "E":
                end = (x, y)
    return start, end


def print_path(field, path):
    for step in path:
        x, y = step
        field[x][y] = "S"
    for line in field:
        print("".join(line))
    print()
    for step in path:
        x, y = step
        field[x][y] = "."


def bfs(field, start_x, start_y, finish_x, finish_y):
    path = [(start_x, start_y)]
    routes = []
    visited = {}

    queue = deque([(start_x, start_y, path, 0, 0)])
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    while queue:
        x, y, path, score, direction = queue.popleft()

        if (x, y) == (finish_x, finish_y):
            routes.append((path, score))
            continue

        # Prune!
        # For part 1 you could use <=, which is WAY faster.
        # But we need all BEST routes for part 2, so we don't
        if ((x, y), direction) in visited and visited[((x, y), direction)] < score:
            continue

        visited[((x, y), direction)] = score

        for key, (dx, dy) in enumerate(dirs):
            new_x, new_y = x + dx, y + dy
            if field[new_x][new_y] != "#" and (new_x, new_y) not in path:
                if key == direction:
                    queue.append(
                        (new_x, new_y, path + [(new_x, new_y)], score + 1, key)
                    )
                else:
                    queue.append(
                        (new_x, new_y, path + [(new_x, new_y)], score + 1001, key)
                    )

    return routes


# Calling the functions
content = lineReader()
field = build_array(content)
(start_x, start_y), (finish_x, finish_y) = find_race(field)
routes = bfs(field, start_x, start_y, finish_x, finish_y)

# part 1
best_score = min(r[1] for r in routes)
print(best_score)

# part 2
best_routes = [r for r in routes if r[1] == best_score]
tiles = {tile for route in best_routes for tile in route[0]}
print(len(tiles))
