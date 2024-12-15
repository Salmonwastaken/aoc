from aoc.helpers.lineReader import lineReader


def buildArray(content: list) -> list:
    return [list(line) for line in content]


def find_start(field):
    for key, line in enumerate(field):
        if "@" in line:
            return key, line.index("@")


def create_new_field(field):
    new_field = [[[] for _ in range(len(field[0] * 2))] for _ in range(len(field))]

    for x, line in enumerate(field):
        for y, c in enumerate(line):
            if c == "#":
                first_val, second_val = "#", "#"
            elif c == "O":
                first_val, second_val = "[", "]"
            elif c == ".":
                first_val, second_val = ".", "."
            elif c == "@":
                first_val, second_val = "@", "."
            new_field[x][y * 2], new_field[x][y * 2 + 1] = first_val, second_val

    return new_field


def push(field, start_x, start_y, dx, dy):
    start_field = field[start_x][start_y]

    if start_field == "[":
        box = ((start_x, start_y), (start_x, start_y + 1))
    elif start_field == "]":
        box = ((start_x, start_y - 1), (start_x, start_y))

    if next_field == "#":
        print("Do Nothing")
    elif next_field == ".":
        print("Move box to new node")
    elif next_field == "[" or next_field == "]":
        print("Another box, let's see if we can push it")


if __name__ == "__main__":
    content = lineReader()
    mid = content.index("")
    instructions = "".join(content[mid + 1 :])
    field = buildArray(content[:mid])

    instruction_translator = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

    # Original field
    for line in field:
        for c in line:
            print(c, end=" ")
        print()
    print()
    # Create new field
    field = create_new_field(field)
    # New field
    for line in field:
        for c in line:
            print(c, end=" ")
        print()
    print()

    x, y = find_start(field)

    for instruction in instructions:
        dx, dy = instruction_translator[instruction]
        next_x, next_y = x + dx, y + dy

        next_field = field[next_x][next_y]

        if next_field == "#":
            print("Do Nothing")
        elif next_field == ".":
            print("Move robot to new node")
            field[next_x][next_y], field[x][y] = field[x][y], field[next_x][next_y]
            x, y = next_x, next_y
        elif next_field == "[" or next_field == "]":
            push(field, x + dx, y + dx, dx, dy)
            print("Attempt to push")

        for line in field:
            for c in line:
                print(c, end=" ")
            print()
        print()

    # Find closest/leftmost edge of every box
    boxes = [
        (x, y)
        for x, line in enumerate(field)
        for y, val in enumerate(line)
        if val == "["
    ]

    total = 0
    for box_x, box_y in boxes:
        total += box_x * 100 + box_y

    print(total)
