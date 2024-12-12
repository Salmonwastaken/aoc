from aoc.helpers.lineReader import lineReader
from collections import defaultdict
from dataclasses import dataclass
from itertools import product

vertical = [(-1, 0), (1, 0)]
horizontal = [(0, -1), (0, 1)]
DIRECTIONS = vertical + horizontal


@dataclass
class Region:
    crop: str
    coordinates: list
    perimeter: int = 0
    sides: int = 0
    area: int = 0
    price: int = 0


def checkBounds(array: list, x: int, y: int) -> bool:
    return 0 <= x < len(array) and 0 <= y < len(array[0])


def buildArray(content: list) -> list:
    return [list(line) for line in content]


def isValid(array: list, x: int, y: int, region, crop) -> bool:
    return checkBounds(array, x, y) and (x, y) not in region and array[x][y] == crop


def dfs(grid, startX, startY, crop):
    region = [(startX, startY)]
    perimeters = []
    stack = [(startX, startY, [(startX, startY)], crop)]

    while stack:
        x, y, path, current_digit = stack.pop()

        for dx, dy in DIRECTIONS:
            next_x, next_y = x + dx, y + dy

            if isValid(grid, next_x, next_y, region, crop):
                region.append((next_x, next_y))
                stack.append((next_x, next_y, region, crop))
            elif (next_x, next_y) not in region:
                perimeters.append((next_x, next_y))

    return region, perimeters


def parse(field):
    visited = [[False for _ in line] for line in content]
    regions = list()

    for x, line in enumerate(field):
        for y, crop in enumerate(line):
            if not visited[x][y]:
                patch, perimeters = dfs(field, x, y, crop)
                # if crop == "B":
                #     print(perimeters)
                #     find_sides(patch, perimeters)
                #     exit()
                # else:
                #     continue
                region = Region(
                    crop=crop,
                    coordinates=patch,
                    area=len(patch),
                    perimeter=len(perimeters),
                    sides=find_sides(patch, perimeters),
                )
                regions.append(region)
                for locationx, locationy in region.coordinates:
                    visited[locationx][locationy] = True

    return regions


def price1(regions):
    total = 0
    for region in regions:
        region.price = region.area * region.perimeter
        total += region.price

    return total


if __name__ == "__main__":
    content = lineReader()

    field = buildArray(content)

    regions = parse(field)

    for region in regions:
        print(
            f"{region.crop} has {region.sides} sides and this patch {region.coordinates}"
        )

    p1 = price1(regions)
    print(f"Part 1: {p1}")
    # p2 = price2(regions)
    # print(f"Part 2: {p2}")
