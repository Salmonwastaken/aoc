from aoc.helpers.lineReader import lineReader

content = lineReader()

# Part 1
answer = 0
for bank in content:
    # (index, digit)
    largest = (0, 0)
    second_largest = 0

    # find largest number in array
    for pos, battery in enumerate(bank):
        # unless its last index
        if pos + 1 == len(bank):
            continue

        b = int(battery)

        if b > largest[1]:
            largest = (pos, b)

    # then find largest number after that pos in array
    for battery in bank[largest[0] + 1 :]:
        b = int(battery)

        if b > second_largest:
            second_largest = b

    largest_battery = int(str(largest[1]) + str(second_largest))
    answer += largest_battery

print(f"Part 1: {answer}")


# Part 2
def find_next_largest(bank, remaining_length):
    next_number = 0
    for pos, battery in enumerate(bank):
        # If current position would make us unable to fill out the battery, end the loop and use the previous result
        if len(bank[pos:]) < remaining_length:
            break

        b = int(battery)

        if b > next_number:
            next_number = b
            # Just fill anything we can't use with 0s
            for i in range(0, pos + 1):
                bank[i] = "0"

    return bank, next_number


answer = 0

# Find next largest digit, until we've filled out all 12 digits
pos = -1
for bank in content:
    battery = ""
    remaining_length = 12
    while len(battery) < 12:
        bank, num = find_next_largest(list(bank), remaining_length)
        battery += str(num)
        remaining_length -= 1
    answer += int(battery)

print(f"Part 2: {answer}")
