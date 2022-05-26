from collections import defaultdict, Counter
from os import path

with open("input_small.txt", "r") as input_file:
    lines = input_file.read().strip().split("\n")

connection_pairs = (l.split("-") for l in lines)
connections_dict = defaultdict(list)

for f, to in connection_pairs:
    if f != "end" and to != "start":
        connections_dict[f].append(to)
    if f != "start" and to != "end":
        connections_dict[to].append(f)


def get_all_paths(start, path_so_far, visited_caves_set, visited_something_twice):
    if start == "end":
        return [path_so_far]
    paths = []
    for dest in connections_dict[start]:
        if dest == 'end':
            paths.append(path_so_far)
            continue
        if dest.islower():
            if dest not in visited_caves_set:
                paths.extend(get_all_paths(dest, path_so_far + [dest], set.union(visited_caves_set, {dest}), visited_something_twice))
            elif visited_something_twice is False:
                paths.extend(get_all_paths(dest, path_so_far + [dest], visited_caves_set, True))
        else:
            paths.extend(get_all_paths(dest, path_so_far + [dest], visited_caves_set, visited_something_twice))
    return paths

paths = get_all_paths("start", [], set(), False)
print(len(paths))

# for p in paths:
#     print(p)

# print(len(paths))
