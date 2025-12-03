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

    # Old method where you just loop over everything, takes 2+ seconds
    # x = 0
    # while x < amount:
    #     location = eval(str(location) + op + str(1))
    #     location = location % 100
    #     if location == 0:
    #         answer += 1
    #     x += 1

    # Faster method

    # eg 407 becomes 7, we just skip looping 400 times for a predetermined outcome
    # This makes real input go from 2s to 0.7s
    roundtrips = amount // 100
    answer += roundtrips
    amount -= roundtrips * 100

    # Check wether we start from 0 and if our action crosses the 0 threshold.
    # This knocks it down to 0.09s
    end_location = eval(str(location) + op + str(amount))
    if (end_location <= 0 and location != 0) or (end_location >= 100 and location != 0):
        last_answer = answer
        answer += 1
    location = end_location % 100


print(f"Part 2: {answer}")
