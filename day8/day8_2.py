def produce_mapping(digits: str):
    digits = [set(d) for d in digits.split()]

    d1 = next(d for d in digits if len(d) == 2)
    d4 = next(d for d in digits if len(d) == 4)
    d7 = next(d for d in digits if len(d) == 3)
    d8 = next(d for d in digits if len(d) == 7)
    d9 = next(d for d in digits if len(d) == 6 and len(d.difference(d4)) == 2)

    left_bottom_segment = next(iter(d8.difference(d9)))
    d2 = next(d for d in digits if len(d) == 5 and left_bottom_segment in d)
    d3 = next(d for d in digits if len(d) == 5 and d.issubset(d9) and d1.issubset(d))
    d5 = next(d for d in digits if len(d) == 5 and d != d2 and d != d3)
    d0 = next(d for d in digits if len(d) == 6 and d.issuperset(d7) and d != d9)
    d6 = next(d for d in digits if len(d) == 6 and d != d0 and d != d9)

    return [(d0, 0), (d1, 1), (d2, 2), (d3, 3), (d4, 4), (d5, 5), (d6, 6), (d7, 7), (d8, 8), (d9, 9)]

def get_digits_inner(mapping, input):
    for i in [set(i) for i in input.split()]:
        print(i)
        yield next(str(d) for s, d in mapping if s == i)

def get_digits(mapping, input):
    return int(''.join(get_digits_inner(mapping, input)))

def get_digits_from_line(line):
    p1, p2 = line.split('|')
    mapping = produce_mapping(p1)
    input = p2
    print(mapping)
    print(line)
    return get_digits(mapping, input)

with open("input.txt", "r") as input_file:
    lines = input_file.read().strip().split("\n")

# get_digits_from_line("dcaf cd cdeabf cefab fgbde efbdc bcd eadcgb gebcadf caegbf | eacfgb cd feacb eafdcbg")

res = sum(get_digits_from_line(l) for l in lines)

print(res)

# def get_len(input_line):
#     inputs = input_line.split("|")[1].split()
#     result = len([input for input in inputs if len(input) in [2, 3, 4, 7]])
#     return result

# lens = (get_len(line) for line in lines)
# print(sum(lens))
