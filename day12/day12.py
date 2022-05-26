from collections import defaultdict, Counter
from os import path

with open("input.txt", "r") as input_file:
    lines = input_file.read().strip().split("\n")

connection_pairs = (l.split("-") for l in lines)
connections_dict = defaultdict(list)

for f, to in connection_pairs:
    if f != "end" and to != "start":
        connections_dict[f].append(to)
    if f != "start" and to != "end":
        connections_dict[to].append(f)


def get_all_paths(start, path_so_far, visited_caves_dict):
    if start == "end":
        return [path_so_far]
    paths = []
    for dest in connections_dict[start]:
        if dest == 'end':
            paths.append(path_so_far)
            continue
        if dest.islower():
            if dest not in visited_caves_dict or visited_caves_dict[dest] == 1:
                if dest not in visited_caves_dict:
                    new_dict = {**visited_caves_dict, dest: 1}
                else:
                    new_dict = {**visited_caves_dict, dest: 2}
                paths.extend(get_all_paths(dest, path_so_far + [dest], new_dict))
        else:
            paths.extend(get_all_paths(dest, path_so_far + [dest], visited_caves_dict))
    return paths

def has_only_sinngle_double_cell(path):
    c = Counter(path)
    count_multiple = 0
    for k, v in c.items():
        if k.islower() and v == 2:
            count_multiple += 1
        if count_multiple > 1:
            return False
    return True

paths = get_all_paths("start", [], dict())
print(len(paths))

paths_filtered = [p for p in paths if has_only_sinngle_double_cell(p)]

for p in paths_filtered:
    print(p)

print(len(paths_filtered))
