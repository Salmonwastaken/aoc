from aoc.helpers.lineReader import lineReader
from tqdm import tqdm


def partial_match(string, sub_string):
    return string[: len(sub_string)] == sub_string


def count_valid_combinations(towels, pattern):
    dp = [0] * (len(pattern) + 1)
    dp[0] = 1

    for i in range(1, len(pattern) + 1):
        for towel in towels:
            if i >= len(towel) and pattern[i - len(towel) : i] == towel:
                dp[i] += dp[i - len(towel)]

    return dp[len(pattern)]


content = lineReader()

towels = list(map(str.lstrip, content[0].split(",")))
patterns = content[2:]

total_ways = 0

for pattern in tqdm(patterns):
    ways = count_valid_combinations(towels, pattern)
    total_ways += ways
    # print(f"Pattern '{pattern}' can be formed in {ways} different ways")

print(total_ways)
