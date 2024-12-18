from aoc.helpers.lineReader import lineReader


def buildArray(content: list) -> list:
    return [list(line) for line in content]


def find_start(field):
    for key, line in enumerate(field):
        if "@" in line:
            return key, line.index("@")


def parse_step(x, y, dx, dy):
    moves = []
    i = 1
    while True:
        next_x, next_y = x + (dx * i), y + (dy * i)
        next_field = field[next_x][next_y]
        # Blockade found, no moves to be made
        if next_field == "#":
            return []
        # Found an empty spot before hitting a wall (with or without boxes)
        if next_field == ".":
            moves.append((next_x, next_y))
            return moves
        # Boxes found
        if next_field == "O":
            moves.append((next_x, next_y))
            i += 1

    # Shouldnt hit?
    return False


if __name__ == "__main__":
    content = lineReader()
    mid = content.index("")
    instructions = "".join(content[mid + 1 :])
    field = buildArray(content[:mid])

    x, y = find_start(field)

    instruction_translator = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

    # for line in field:
    #     for c in line:
    #         print(c, end=" ")
    #     print()

    for instruction in instructions:
        # print(x, y)
        # print(instruction)
        # print(instruction_translator)
        dx, dy = instruction_translator[instruction]
        # print(dx, dy)
        moves = parse_step(x, y, dx, dy)
        # print(moves)
        # Nothing to do
        if moves == []:
            continue

        # Swap all the boxes into their new position
        for new_x, new_y in moves:
            field[x][y], field[new_x][new_y] = field[new_x][new_y], field[x][y]

        x, y = x + dx, y + dy
        # for line in field:
        #     for c in line:
        #         print(c, end=" ")
        #     print()

    # Find all the boxes
    boxes = [
        (x, y)
        for x, line in enumerate(field)
        for y, val in enumerate(line)
        if val == "O"
    ]
    total = 0
    for box_x, box_y in boxes:
        total += box_x * 100 + box_y

    print(total)
