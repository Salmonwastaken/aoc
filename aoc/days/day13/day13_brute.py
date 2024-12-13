from aoc.helpers.lineReader import lineReader
import re

# Only works for part 1 ofcourse
# But an okay way to troubleshoot your actual solutions...


def bruteforce(a_x, a_y, b_x, b_y, p_x, p_y):
    for a in range(100):
        step_a_x = a_x * a
        step_a_y = a_y * a
        for b in range(100):
            step_b_x = b_x * b
            step_b_y = b_y * b

            total_x = step_a_x + step_b_x
            total_y = step_a_y + step_b_y

            if total_x == p_x and total_y == p_y:
                return a, b

    return 0, 0


if __name__ == "__main__":
    content = lineReader(False)

    number_regex = re.compile(r"\d+")
    machines = content.strip().split("\n\n")
    total_cost = 0

    for machine in machines:
        numbers = [int(x) for x in re.findall(number_regex, machine)]
        a, b = bruteforce(*numbers)

        cost = a * 3 + b
        total_cost += cost

    print(total_cost)
