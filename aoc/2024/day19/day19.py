from aoc.helpers.lineReader import lineReader
from tqdm import tqdm
from collections import deque


def partial_match(string, sub_string):
    return string[: len(sub_string)] == sub_string


def has_valid_combination(towels, pattern):
    # Secretly a BFS, don't tell anyone!
    max_length = len(pattern)

    queue = deque([""])
    seen = set([""])

    while queue:
        seq = queue.popleft()

        for towel in towels:
            new_str = seq + towel

            if len(new_str) <= max_length and partial_match(pattern, new_str):
                if new_str == pattern:
                    return True
                if new_str not in seen:
                    seen.add(new_str)
                    queue.append(new_str)

    return False


content = lineReader()

towels = list(map(str.lstrip, content[0].split(",")))
patterns = content[2:]

possible_towels = 0

for pattern in tqdm(patterns):
    if has_valid_combination(tuple(towels), pattern):
        possible_towels += 1


print(possible_towels)
