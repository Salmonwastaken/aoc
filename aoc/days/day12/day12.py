from aoc.helpers.lineReader import lineReader
from dataclasses import dataclass

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


def countCorners(grid, area, crop):
    corners = 0

    directions = {
        #       NW       N      W
        "NW": (-1, -1, -1, 0, 0, -1),
        #        NE      N     E
        "NE": (-1, 1, -1, 0, 0, 1),
        #        SW     W      S
        "SW": (1, -1, 0, -1, 1, 0),
        #       SE     E     S
        "SE": (1, 1, 0, 1, 1, 0),
    }

    for x, y in area:
        for _, (x1, y1, x2, y2, x3, y3) in directions.items():
            corner_x, corner_y = x + x1, y + y1
            side1_x, side1_y = x + x2, y + y2
            side2_x, side2_y = x + x3, y + y3

            corner_value = (
                grid[corner_x][corner_y]
                if checkBounds(grid, corner_x, corner_y)
                else "."
            )

            side1_value = (
                grid[side1_x][side1_y] if checkBounds(grid, side1_x, side1_y) else "."
            )

            side2_value = (
                grid[side2_x][side2_y] if checkBounds(grid, side2_x, side2_y) else "."
            )

            if corner_value != crop and side1_value == crop and side2_value == crop:
                corners += 1
            elif corner_value != crop and side1_value != crop and side2_value != crop:
                corners += 1
            elif corner_value == crop and side1_value != crop and side2_value != crop:
                corners += 1

    return corners


def parse(field):
    visited = [[False for _ in line] for line in content]
    regions = list()

    for x, line in enumerate(field):
        for y, crop in enumerate(line):
            if not visited[x][y]:
                patch, perimeters = dfs(field, x, y, crop)
                region = Region(
                    crop=crop,
                    coordinates=patch,
                    area=len(patch),
                    perimeter=len(perimeters),
                    sides=countCorners(field, patch, crop),
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


def price2(regions):
    total = 0
    for region in regions:
        region.price = region.area * region.sides
        total += region.price

    return total


if __name__ == "__main__":
    content = lineReader()

    field = buildArray(content)

    regions = parse(field)

    p1 = price1(regions)
    print(f"Part 1: {p1}")
    p2 = price2(regions)
    print(f"Part 2: {p2}")
