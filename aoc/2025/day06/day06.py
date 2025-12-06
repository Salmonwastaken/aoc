from aoc.helpers.lineReader import lineReader
import re
import time

# Part 1
s = time.perf_counter()
content = lineReader()

lines = []
# Grab all numbers while removing all whitespace
for line in content:
    a = [x for x in line.split(" ") if x != '']
    lines.append(a)

# Seperate the operators into it's own list
ops = lines.pop()

answer = 0
# Build the equation as a string by adding every number for a position from the list
# then add the current operator, except if it's the final number of the current equation
for pos, op in enumerate(ops):
    equation = ""
    for line in lines:
        equation += (line[pos])
        if line != lines[-1]:
            equation += f"{op} "


    a = eval(equation)
    answer += a

print(f"Part 1 took: {(time.perf_counter() - s):.6f}s")
print(f"Part 1: {answer}\n")

# Part 2
s = time.perf_counter()
content = lineReader()
# Grab all operators + whitespace, so we can use it to determine column length
ops = list(re.findall(r"\W\s+", content.pop()))

answer = 0
for pos, op in enumerate(ops):
    # Determine current column length, can differ per column for real input
    length = len(op)-1
    column = []
    
    # Then for every line we have, grab the current relevant number and delete them from the greater content
    for key, line in enumerate(content):
        a, content[key] = line[:length], line[length+1:]
        column.append(a)
    
    # Loop over every number from right-to-left
    # If it isn't whitespace, add it or assign to the number for that specific column.
    numbers = {}
    for number in column:
        for x in range(1, length+1):
            if number[-x] != " ":
                try:
                    numbers[x] += number[-x]
                except KeyError:
                    numbers[x] = str(number[-x])

    numbers = dict(sorted(numbers.items()))
    
    # Build the equation by dumping it into a string and passing it to eval
    # Same as part 1, except we didn't strip the operator before
    equation = ""
    for number in numbers.values():
        equation += number
        if number != numbers[len(numbers.keys())]:
            equation += f"{op.strip()}"

    a = eval(equation)
    answer += a

print(f"Part 2 took: {(time.perf_counter() - s):.6f}s")
print(f"Part 2: {answer}\n")
