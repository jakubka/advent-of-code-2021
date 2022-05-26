from collections import Counter

with open("input_small.txt", "r") as input_file:
    lines = input_file.read().strip().split("\n")

template_str = lines[0]

template_dict = {
    (l[0], l[1]): r for l, r in (l.split(" -> ") for l in lines if "->" in l)
}


def gen_between_two(start, end, depth_left):
    if depth_left == 0:
        yield start
    else:
        new_char = template_dict[(start, end)]
        yield from gen_between_two(start, new_char, depth_left - 1)
        yield from gen_between_two(new_char, end, depth_left - 1)


def generate_polymer_from_str(pol_str, depth):
    for i in range(len(pol_str) - 1):
        yield from gen_between_two(pol_str[i], pol_str[i + 1], depth)
    yield pol_str[-1]


def generate_polymer_from_tuple(tuple, depth):
    yield from gen_between_two(tuple[0], tuple[1], depth)
    yield tuple[1]


def get_unique_pairs(polymer):
    pairs = set((polymer[i], polymer[i + 1]) for i in range(len(polymer) - 1))
    return pairs


pairs = get_unique_pairs(list(generate_polymer_from_str(template_str, 10)) + ["N", "N"])

pol10_dict = {p: list(generate_polymer_from_tuple(p, 10)) for p in pairs}


def gen_between_two_10(start, end, depth_left):
    if depth_left == 0:
        yield start
    else:
        new_polymer_10 = pol10_dict[(start, end)]
        for i in range(len(new_polymer_10) - 1):
            yield from gen_between_two_10(
                new_polymer_10[i], new_polymer_10[i + 1], depth_left - 1
            )


def gen_polymer_20(start, end):
    return gen_between_two_10(start, end, 2)


def generate_polymer_20_from_str(pol_str):
    for i in range(len(pol_str) - 1):
        yield from gen_polymer_20(pol_str[i], pol_str[i + 1])
    yield pol_str[-1]


def count_char(polymer, char):
    s = 0
    for c in polymer:
        if c == char:
            s += 1
    return s


polymer_20_char_dict = {(s, e): count_char(gen_polymer_20(s, e), "B") for s, e in pairs}

basic_pol20 = list(generate_polymer_20_from_str(template_str))
s = 0
for i in range(len(basic_pol20) - 1):
    s += polymer_20_char_dict[(polymer_20_char_dict[i], polymer_20_char_dict[i + 1])]
print(s)

# print(polymer_20_char_dict)

# polymer_20 = list(gen_polymer_20("N", "N"))
# print(len(polymer_20), polymer_20[:10], polymer_20[-1])

# polymer_20_2 = list(generate_polymer_from_tuple(("N", "N"), 20))
# print(len(polymer_20_2), polymer_20_2[:10], polymer_20_2[-1])

# pol20 = list(generate_polymer_from_str(template_str, 10))

# print(len(pol20))
# print(len(get_unique_pairs(pol20)))

# s = 0
# for c in generate_polymer_from_str("NNCB", 20):
#     if c == 'N':
#         s += 1
# print(s)

# x   y
# x a y
