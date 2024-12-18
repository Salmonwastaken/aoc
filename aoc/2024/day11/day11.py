from aoc.helpers.lineReader import lineReader
from collections import defaultdict


def findMiddle(string: str) -> int:
    return len(string) // 2


def parse(stones: dict, iterations: int) -> dict:
    for i in range(iterations):
        for stone, count in list(stones.items()):
            # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
            # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
            # The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone.
            # (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
            # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
            if stone == "0":
                stones["1"] += count
                stones[stone] -= count
            elif len(stone) % 2 == 0:
                middle = findMiddle(stone)
                left = stone[:middle].lstrip("0") or "0"
                right = stone[middle:].lstrip("0") or "0"
                stones[left] += count
                stones[right] += count
                stones[stone] -= count
            else:
                stones[str(int(stone) * 2024)] += count
                stones[stone] -= count

    return sum(stones.values())


if __name__ == "__main__":
    content = lineReader(False)
    initial = content.split()

    initial_stones = defaultdict(int)

    for stone in initial:
        initial_stones[stone] += 1

    # Make a copy to not fuck with the inital input the first time
    p1 = parse(initial_stones.copy(), 25)
    print(f"Part 1: {p1}")
    # Save yourself the copy overhead on the last run
    p2 = parse(initial_stones, 75)
    print(f"Part 2: {p2}")
