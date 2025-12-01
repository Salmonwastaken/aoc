from aoc.helpers.lineReader import lineReader

dialtable = lineReader()

# Part 1
location = 50
answer = 0
for rotation in dialtable:
    direction = rotation[0]
    amount = int(rotation[1:])

    if direction == "L":
        location -= amount
    else:
        location += amount

    location = location % 100

    if location == 0:
        answer += 1

print(f"Part 1: {answer}")

# Part 2
location = 50
answer = 0
for rotation in dialtable:
    direction = rotation[0]
    amount = int(rotation[1:])

    if direction == "L":
        op = "-"
    else:
        op = "+"

    x = 0
    while x < amount:
        location = eval(str(location) + op + str(1))
        location = location % 100
        if location == 0:
            answer += 1
        x += 1

print(f"Part 2: {answer}")
