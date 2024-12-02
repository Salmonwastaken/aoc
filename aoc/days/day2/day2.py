from aoc.helpers.lineReader import lineReader


def validDistance(c):
    match abs(c):
        case 1 | 2 | 3:
            return True
        case _:
            return False


def determineDirection(c):
    # 0 = Neutral
    # 1 = Increasing
    # 2 = Decreasing
    match c:
        case c if c > 0:
            return 1
        case c if c < 0:
            return 2
        case _:
            return 0


def validDirection(d, ed):
    if d is not ed:
        return False

    return True


def parse(res):
    for k, v in enumerate(res):
        if k == 0:
            expected_direction = 0
            change = int(res[k + 1]) - int(v)
        else:
            change = int(v) - int(res[k - 1])

        if not validDistance(change):
            return False, k

        direction = determineDirection(change)

        if expected_direction == 0:
            expected_direction = direction
            continue

        if not validDirection(direction, expected_direction):
            return False, k

    return True, None


def counter(res, index):
    new_res = [s for i, s in enumerate(res) if i != index]
    valid, _ = parse(new_res)
    return valid


def part1(content):
    safeReports = 0

    for line in content:
        res = line.split()
        valid, _ = parse(res)

        if valid:
            safeReports += 1

    return safeReports


def part2(content):
    safeReports = 0

    for line in content:
        res = line.split()
        valid, failedIndex = parse(res)

        if valid:
            safeReports += 1
        else:
            failureOptions = [-1, 0, 1]
            if any(counter(res, failedIndex - i) for i in failureOptions):
                safeReports += 1
            elif counter(res, 0) or counter(res, -1):
                safeReports += 1

    return safeReports


if __name__ == "__main__":
    content = lineReader()

    part1 = part1(content)
    print(f"Part 1: {part1}")
    part2 = part2(content)
    print(f"Part 2: {part2}")
