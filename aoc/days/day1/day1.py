from aoc.helpers.lineReader import lineReader

content = lineReader()

left_numbers = []
right_numbers = []

for line in content:
  s = line.split()
  left_numbers.append(int(s[0]))
  right_numbers.append(int(s[1]))

def part1(left_numbers, right_numbers):
  left_numbers.sort()
  right_numbers.sort()

  total_distance = 0

  for k, v in enumerate(left_numbers):
    result = abs(v - right_numbers[k])
    total_distance += result

  print(total_distance)

part1(left_numbers, right_numbers)

def part2(left_numbers, right_numbers):
  similarity_score = 0

  for v in left_numbers:
    amount = right_numbers.count(v)
    similarity_score += (v * amount)

  print(similarity_score)

part2(left_numbers, right_numbers)
