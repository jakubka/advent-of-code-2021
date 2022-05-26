from abc import ABC
from collections import Counter, defaultdict

with open("input.txt", "r") as input_file:
    lines = input_file.read().strip().split("\n")

template_str = lines[0]

rules = {l: [l[0] + r, r + l[1]] for l, r in (l.split(" -> ") for l in lines[2:])}

polymer_pair_counts = defaultdict(int)
for i in range(len(template_str) - 1):
    polymer_pair_counts[template_str[i] + template_str[i + 1]] += 1

for _ in range(40):
    new_polymer = defaultdict(int)
    for pair, count in polymer_pair_counts.items():
        rule = rules[pair]
        new_polymer[rule[0]] += count
        new_polymer[rule[1]] += count
    polymer_pair_counts = new_polymer

counts = defaultdict(int)
for pair, count in polymer_pair_counts.items():
    counts[pair[0]] += count
counts[template_str[-1]] += 1
elements = sorted([count for count in counts.values()])
print(elements[-1] - elements[0])
