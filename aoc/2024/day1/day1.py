from collections import Counter

from aoc.helpers.lineReader import lineReader


def parse_input(content: list[str]) -> tuple[list[int], list[int]]:
    left_numbers = []
    right_numbers = []

    for line in content:
        s = line.split()
        left_numbers.append(int(s[0]))
        right_numbers.append(int(s[1]))

    return left_numbers, right_numbers


def part1(left_numbers: list[int], right_numbers: list[int]) -> int:
    left_sorted = sorted(left_numbers)
    right_sorted = sorted(right_numbers)

    total_distance = sum(
        abs(left - right) for left, right in zip(left_sorted, right_sorted)
    )
    return total_distance


def part2(left_numbers: list[int], right_numbers: list[int]) -> int:
    right_counts = Counter(right_numbers)

    similarity_score = sum(v * right_counts[v] for v in left_numbers)
    return similarity_score


if __name__ == "__main__":
    content = lineReader()
    left_numbers, right_numbers = parse_input(content)

    total_distance = part1(left_numbers, right_numbers)
    print(f"Total Distance: {total_distance}")

    similarity_score = part2(left_numbers, right_numbers)
    print(f"Similarity Score: {similarity_score}")
