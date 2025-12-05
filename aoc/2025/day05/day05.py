from aoc.helpers.lineReader import lineReader
import time

s = time.perf_counter()
content = lineReader()

split_index = content.index("")
ranges = dict(
    sorted((int(i), int(v)) for i, v in (x.split("-") for x in content[:split_index]))
)
ingredient_ids = [int(x) for x in content[split_index + 1 :]]

merged_ranges = {}
# range start, range end
for rs, re in ranges.items():
    if not merged_ranges:
        merged_ranges[rs] = re
        continue

    last_start = max(merged_ranges.keys())
    last_end = merged_ranges[last_start]

    # Example:
    # current last: 10-20
    # actions if new is:
    # 6-18; impossible, because input is sorted hence no need for additional bound checking
    # 11-18; 11 <= 19 (True); max(20, 18); merged_ranges[10] = 18
    # 21-25; 21 <= 21 (True); max(20, 25); merged_ranges[10] = 25
    # 22-30; 22 <= 30 (False); merged_ranges[22] = 30
    if rs <= last_end + 1:
        merged_ranges[last_start] = max(last_end, re)
    else:
        merged_ranges[rs] = re

print(f"Shared prep took: {(time.perf_counter() - s):.6f}s\n")

s = time.perf_counter()
answer = sum(
    any(start <= ingredient <= end for start, end in merged_ranges.items())
    for ingredient in ingredient_ids
)

print(f"Part 1 took: {(time.perf_counter() - s):.6f}s")
print(f"Part 1: {answer}\n")

s = time.perf_counter()
answer = sum((mre - mrs) + 1 for mrs, mre in merged_ranges.items())

print(f"Part 2 took: {(time.perf_counter() - s):.6f}s")
print(f"Part 2: {answer}\n")
