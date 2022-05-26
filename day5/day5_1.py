import re
from collections import defaultdict


def get_coords():
    with open("input.txt", "r") as input_file:
        lines = input_file.read().split("\n")
    lines_parsed = (re.match(r"(\d+),(\d+) -> (\d+),(\d+)", line) for line in lines)
    lines_parsed = (line.groups() for line in lines_parsed if line is not None)
    lines_parsed = (
        (int(x1), int(y1), int(x2), int(y2)) for x1, y1, x2, y2 in lines_parsed
    )
    lines_parsed = (
        (x1, y1, x2, y2) for x1, y1, x2, y2 in lines_parsed if x1 == x2 or y1 == y2
    )
    return lines_parsed


coords = get_coords()

visited_coords = defaultdict(int)
for x1, y1, x2, y2 in coords:
    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            visited_coords[f"{x1}_{y}"] += 1
    if y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            visited_coords[f"{x}_{y1}"] += 1

print(len([val for val in visited_coords.values() if val > 1]))
