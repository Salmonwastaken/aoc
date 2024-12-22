from aoc.helpers.lineReader import lineReader

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+


#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+


def is_valid(x, y, kind):
    return COMBINED[kind][(" ")] != (x, y)


def converter(code, kind):
    # Starting location
    x, y = COMBINED[kind]["A"]
    seq = ""
    for number in code:
        # Goal
        nx, ny = COMBINED[kind][number]
        # Difference
        dx, dy = nx - x, ny - y
        # Intermediate coordinates.
        # Used to make sure we don't go on the invalid space
        ix, iy = x, y
        # Move until we're in the right spot
        while (dx, dy) != (0, 0):
            # There's an implicit ordering here which should result in lower moves in later steps
            if dy < 0 and is_valid(ix, iy - 1 * abs(dy), kind):
                iy += -1 * abs(dy)
                seq += "<" * abs(dy)
                dy += 1 * abs(dy)

            if dx < 0 and is_valid(ix - 1 * abs(dx), iy, kind):
                ix += -1 * abs(dx)
                seq += "^" * abs(dx)
                dx += 1 * abs(dx)
            if dx > 0 and is_valid(ix + 1 * abs(dx), iy, kind):
                ix += 1 * abs(dx)
                seq += "v" * abs(dx)
                dx += -1 * abs(dx)

            if dy > 0 and is_valid(ix, iy + 1 * abs(dy), kind):
                iy += 1 * abs(dy)
                seq += ">" * abs(dy)
                dy += -1 * abs(dy)

        seq += "A"

        x, y = nx, ny

    return seq


COMBINED = {
    "numerical": {
        "7": (0, 0),
        "8": (0, 1),
        "9": (0, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "1": (2, 0),
        "2": (2, 1),
        "3": (2, 2),
        " ": (3, 0),
        "0": (3, 1),
        "A": (3, 2),
    },
    "directional": {
        " ": (0, 0),
        "^": (0, 1),
        "A": (0, 2),
        "<": (1, 0),
        "v": (1, 1),
        ">": (1, 2),
    },
}

content = lineReader()

total = 0

for code in content:
    a = converter(code, "numerical")
    # print(a)
    b = converter(a, "directional")
    # print(b)
    c = converter(b, "directional")
    # print(c)
    number = int("".join(filter(str.isdigit, code)))
    total += len(c) * number

print(total)
