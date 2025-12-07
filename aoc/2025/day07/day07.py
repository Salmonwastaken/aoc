from aoc.helpers.lineReader import lineReader
from aoc.helpers.grid_helpers import build_array, find_index, check_bounds
from collections import defaultdict, deque

content = lineReader()
arr = build_array(content)
start_point = find_index(arr, "S")[0]
splitters = find_index(arr, "^")

# A dict of keys, for easy deduplication i guess
beams = {}

beams[start_point] = True
beams[(start_point[0] +1, start_point[1])] = True
beams[(start_point[0] +2, start_point[1])] = True

part1 = 0
for splitter in splitters:
    x, y = splitters[splitters.index(splitter)]
    
    if (x-1, y) not in beams:
        continue
    
    part1 += 1
    
    for i in [1, -1]:
        sx, sy = x,y+i 
        
        # Skip beams we've already mapped
        if (sx, sy) in beams:
            continue
        
        beams[(sx, sy)] = True
        nsx, nsy = (sx+1, sy)
        while check_bounds(arr, nsx, nsy):
            if arr[nsx][nsy] == "^":
                beams[(nsx, nsy)] = True
                break
            beams[(nsx, nsy)] = True
            nsx, nsy = (nsx+1, nsy)

print(part1)
print()

# part 2
class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]


def toposort(edges):
    indeg = defaultdict(int)
    for u in edges:
        for v in edges[u]:
            indeg[v] += 1

    q = deque([u for u in edges if indeg[u] == 0])
    order = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in edges[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return order

def count_paths(edges, start, goal):
    order = toposort(edges)
    order.reverse()

    dp = {node: 0 for node in edges}
    dp[goal] = 1

    for u in order:
        for v in edges[u]:
            dp[u] += dp[v]

    return dp[start]

graph = SimpleGraph()

dirs = [(-1, 0), (0, -1), (0, 1)]
allowed_dirs = {
    '.^': [(0, 1), (0, -1)],
    '^.': [(-1, 0)],
    '..': [(-1, 0)],
    '.S': [(-1, 0)],
    'S.': []
}

for bx, by in beams:
    graph.edges[(bx,by)] = []
    beam_type = arr[bx][by]
    for dx, dy in dirs:
        nx, ny = bx + dx, by + dy
        if not check_bounds(arr, nx, ny):
            continue
        new_type = arr[nx][ny]
        if (dx, dy) in allowed_dirs[f"{beam_type}{new_type}"] and (nx, ny) in beams.keys():
            graph.edges[(bx,by)].append((nx,ny))


final_row = len(arr) - 1
fr_length = len(arr[-1])

endpoints = []

for i in range(0, fr_length):
    if (final_row, i) in beams:
        endpoints.append((final_row, i))

all_paths = []

total_routes = 0
for end in endpoints:
    total_routes += count_paths(graph.edges, end, start_point)

print(total_routes)