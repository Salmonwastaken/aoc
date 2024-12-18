filename = "input.txt"
f = open(filename)

lines = f.read().splitlines()
total_valid = 0


def isValid(numbers):
    for key, number in enumerate(numbers):
        if key + 1 == len(numbers):
            continue

        next_number = numbers[key + 1]

        difference = number - next_number
        if difference >= 1:
            direction = "omhoog"
        elif difference <= -1:
            direction = "omlaag"
        else:
            return False

        if key == 0:
            expected_direction = direction
        elif expected_direction != direction:
            return False

        if not (abs(difference) >= 1 and abs(difference) <= 3):
            return False

    return True


for line in lines:
    numbers = [int(i) for i in line.split()]
    # Create a  bunch of new lists with one number removed
    new_lists = [numbers]
    for index in range(len(numbers)):
        new_list = [value for key, value in enumerate(numbers) if key != index]
        new_lists.append(new_list)
    # check if these new lists are valid or not
    for new_list in new_lists:
        valid = isValid(new_list)
        if valid:
            total_valid += 1
            break

print(total_valid)
