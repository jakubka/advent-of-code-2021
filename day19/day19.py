from collections import defaultdict
import re
from pprint import pprint

with open("input.txt", "r") as input_file:
    lines = input_file.read().strip().split("\n")

beacons_by_scanners = defaultdict(list)

current_scanner = None
for l in lines:
    if "scanner" in l:
        current_scanner = int(re.match("--- scanner (\d+) ---", l).group(1))
    elif "," in l:
        beacons_by_scanners[current_scanner].append([int(d) for d in l.split(",")])

distances_by_scanners = dict()

for scanner, beacons in beacons_by_scanners.items():
    distances = set()
    for b1 in beacons:
        for b2 in beacons:
            if b1 == b2:
                continue
            d = sorted([abs(b1[0] - b2[0]), abs(b1[1] - b2[1]), abs(b1[2] - b2[2])])
            distances.add(tuple(d))
    distances_by_scanners[scanner] = distances

for s1, distances1 in distances_by_scanners.items():
    for s2, distances2 in distances_by_scanners.items():
        if s1 >= s2:
            continue
        same_distances = distances1.intersection(distances2)
        if len(same_distances) > 0:
            print(f'{s1}<>{s2}: {len(same_distances)} same distances')
            # pprint(same_distances)

# pprint(distances_by_scanners)
