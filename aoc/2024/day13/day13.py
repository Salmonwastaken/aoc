from aoc.helpers.lineReader import lineReader
import re


def is_close_enough(num):
    return abs(round(num) - num) < 0.001


def solve(a_x, a_y, b_x, b_y, p_x, p_y):
    # Part 2 bullshit
    p_x += 10000000000000
    p_y += 10000000000000
    slope_a = a_y / a_x

    y_intecept_a = p_y - slope_a * p_x

    slope_b = b_y / b_x

    y_intercept_b = 0

    x_intersection = (y_intercept_b - y_intecept_a) / (slope_a - slope_b)

    b_count = x_intersection / b_x
    a_count = (p_x - x_intersection) / a_x

    solved = is_close_enough(a_count) and is_close_enough(b_count)

    if solved:
        a_count = round(a_count)
        b_count = round(b_count)
        return a_count * 3 + b_count
    # If unsolvable
    return 0


if __name__ == "__main__":
    content = lineReader(False)

    number_regex = re.compile(r"\d+")
    machines = content.strip().split("\n\n")
    total_cost = 0

    for machine in machines:
        numbers = [int(x) for x in re.findall(number_regex, machine)]
        cost = solve(*numbers)
        total_cost += cost

    print(total_cost)
