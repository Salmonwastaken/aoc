from aoc.helpers.lineReader import lineReader
from collections import Counter

def parse_input(content):
  left_numbers = []
  right_numbers = []

  for line in content:
    s = line.split()
    left_numbers.append(int(s[0]))
    right_numbers.append(int(s[1]))

  return left_numbers, right_numbers


def part1(left_numbers, right_numbers):
  left_sorted = sorted(left_numbers)
  right_sorted = sorted(right_numbers)

  total_distance = sum(abs(left - right) for left, right in zip(left_sorted, right_sorted))
  return total_distance


def part2(left_numbers, right_numbers):
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
