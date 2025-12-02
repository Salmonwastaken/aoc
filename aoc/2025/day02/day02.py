from aoc.helpers.lineReader import lineReader

content = lineReader(False)

ranges = content.split(",")

# Part 1
answer = 0
for ids in ranges:
    start, stop = ids.split("-")
    for i in range(int(start), int(stop) + 1):
        half_length = int(len(str(i)) / 2)

        if half_length % 1 != 0:
            continue

        first_half = str(i)[:half_length]
        second_half = str(i)[half_length:]
        if first_half == second_half:
            answer += i

print(answer)

# Part 2
answer = 0
for ids in ranges:
    start, stop = ids.split("-")
    for i in range(int(start), int(stop) + 1):
        length = len(str(i))
        half = int(length / 2)
        for x in range(1, length + 1):
            if x > half:
                continue

            current_text = str(i)[0:x]
            remaining_text = str(i)

            expected_occurences = length / x
            if half % 1 != 0:
                continue

            occurences = remaining_text.count(current_text)

            if expected_occurences == occurences:
                answer += i
                break

print()
print(answer)
