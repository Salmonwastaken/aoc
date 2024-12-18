from aoc.helpers.lineReader import lineReader
from collections import deque, defaultdict


def findMiddle(schedule: list) -> int:
    return len(schedule) // 2


def parseRules(rules: list) -> set:
    return {(rule.split("|")[0], rule.split("|")[1]) for rule in rules}


def parseContent(content: list) -> (list, list):
    split = content.index("")
    rules = content[:split]
    schedules = [schedule.split(",") for schedule in content[split + 1 :]]
    return rules, schedules


def checkSchedules(schedules: list[str], rules_set: set) -> (list[str], list[str]):
    validSchedules = []
    invalidSchedules = []

    for schedule in schedules:
        if isValid(schedule, rules_set):
            validSchedules.append(schedule)
        else:
            invalidSchedules.append(schedule)

    return validSchedules, invalidSchedules


def isValid(schedule: list[str], rules_set: set) -> bool:
    for rule in rules_set:
        X, Y = rule

        if X in schedule and Y in schedule:
            index_X = schedule.index(X)
            index_Y = schedule.index(Y)

            if index_X > index_Y:
                return False

    return True


def calculateSum(schedules: list[str]) -> int:
    total = 0
    for schedule in schedules:
        middleIndex = findMiddle(schedule)
        total += int(schedule[middleIndex])
    return total


def part1(validSchedules: list[str]) -> int:
    return calculateSum(validSchedules)


def sortSchedule(schedule: list[str], rules_set: set) -> list[str]:
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for page in schedule:
        in_degree[page] = 0

    for x, y in rules_set:
        if x in schedule and y in schedule:
            graph[x].append(y)
            in_degree[y] += 1

    # Topological sort using Kahn's algorithm
    # https://www.geeksforgeeks.org/kahns-algorithm-in-python/
    queue = deque([page for page in schedule if in_degree[page] == 0])
    sorted_schedule = []

    while queue:
        node = queue.popleft()
        sorted_schedule.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return sorted_schedule


def part2(invalidSchedules: list[str], rules_set: set) -> int:
    total = 0
    for schedule in invalidSchedules:
        sorted_schedule = sortSchedule(schedule, rules_set)
        middleIndex = findMiddle(sorted_schedule)
        total += int(sorted_schedule[middleIndex])
    return total


if __name__ == "__main__":
    content = lineReader()

    rules, schedules = parseContent(content)
    rules_set = parseRules(rules)

    validSchedules, invalidSchedules = checkSchedules(schedules, rules_set)

    p1 = part1(validSchedules)
    print(f"Part 1: {p1}")

    p2 = part2(invalidSchedules, rules_set)
    print(f"Part 2: {p2}")
