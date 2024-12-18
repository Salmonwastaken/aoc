# Entirely based on https://www.youtube.com/watch?v=zYvZS68tPsU
# Couldn't wrap my head around managing the 2-wide boxes..

with open("input.txt") as fin:
    parts = fin.read().strip().split("\n\n")
    grid = [list(line) for line in parts[0].split("\n")]
    steps = parts[1].replace("\n", "")

dirs = {"<": [0, -1], "v": [1, 0], ">": [0, 1], "^": [-1, 0]}

n = len(grid)

# We collect all the locations of walls and *LEFT* sides of boxes.
boxes = []
walls = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == "@":
            ci, cj = i, j * 2
        elif grid[i][j] == "O":
            boxes.append([i, j * 2])
        elif grid[i][j] == "#":
            walls.append([i, j * 2])
            walls.append([i, j * 2 + 1])


def in_grid(i, j):
    return (0 <= i < n) and (0 <= j < 2 * n)


def move(dir):
    global ci, cj, grid

    newi, newj = ci + dir[0], cj + dir[1]
    # The robot landed outside the grid, which is pretty hard to do aka shouldnt happen
    if not in_grid(newi, newj):
        return

    # The robot would end up in a wall, so we cancel the move
    if [newi, newj] in walls:
        return

    # We see if the next step or the one on the left of it would land us on a left-side of a box (since that's all we track)
    # If we do, we gather it
    stack = []
    if [newi, newj] in boxes:
        stack.append([newi, newj])
    if [newi, newj - 1] in boxes:
        stack.append([newi, newj - 1])

    can_move = True

    # While we found a box, we have to check if there's any boxes connected to it.
    # We use a DFS to find all connected boxes
    seen = set()
    while len(stack) > 0:
        topi, topj = stack.pop()
        ni, nj = topi + dir[0], topj + dir[1]

        if not in_grid(ni, nj):
            can_move = False
            break

        # Running into a wall always means we cannot move at all
        if [ni, nj] in walls or [ni, nj + 1] in walls:
            can_move = False
            break

        # Did we see this box already?
        if (topi, topj) in seen:
            continue
        seen.add((topi, topj))

        # Check if our next step is a place where a box currently is
        # I added some examples, where ( is the current box location and { is the box it would detect
        # This is a left move, <
        ##############
        ##......##..##
        ##..........##
        ##....[][]@.##
        ##....[]....##
        ##..........##
        ##############
        # detects:
        ##############
        ##......##..##
        ##..........##
        ##....{}()@.##
        ##....[]....##
        ##..........##
        ##############
        if [ni, nj] in boxes:
            stack.append([ni, nj])

        # To check for left halves one to the left (eg an upwards move)
        ##############
        ##......##..##
        ##..........##
        ##...[][]...##
        ##....[]....##
        ##.....@....##
        ##############
        # detects:
        ##############
        ##......##..##
        ##..........##
        ##...{}[]...##
        ##....()....##
        ##.....@....##
        ##############
        if [ni, nj - 1] in boxes:
            stack.append([ni, nj - 1])

        # To check for left halves one to the right (eg an upwards move)
        ##############
        ##......##..##
        ##..........##
        ##...[][]...##
        ##....[]....##
        ##.....@....##
        ##############
        # detects:
        ##############
        ##......##..##
        ##..........##
        ##...[]{}...##
        ##....()....##
        ##.....@....##
        ##############
        if [ni, nj + 1] in boxes:
            stack.append([ni, nj + 1])

    # Handling the cases where we can't move the boxes (eg wall)
    if not can_move:
        return

    for i, box in enumerate(boxes):
        # Start moving all the boxes we saw in our DFS
        # By simply adding the direction to their location
        if tuple(box) in seen:
            boxes[i][0] += dir[0]
            boxes[i][1] += dir[1]

    # Update the robot position
    ci += dir[0]
    cj += dir[1]


# Visual representation for debugging
def print_grid(boxes, walls, ci, cj):
    for i in range(n):
        for j in range(n * 2):
            if [i, j] in walls:
                print("#", end="")
            elif [i, j] in boxes:
                print("[", end="")
            elif [i, j - 1] in boxes:
                print("]", end="")
            elif (i, j) == (ci, cj):
                print("@", end="")
            else:
                print(".", end="")
        print()
    print()


print_grid(boxes, walls, ci, cj)

for step in steps:
    move(dirs[step])
    # This bloats the runtime massively on the actual input
    # print_grid(boxes, walls, ci, cj)

print_grid(boxes, walls, ci, cj)

total = 0
for i, j in boxes:
    total += i * 100 + j

print(total)
