with open("input.txt", "r") as input_file:
    lines = input_file.read().strip().split("\n")

openings = {
    '(': ')',
    '[': ']',
    '<': '>',
    '{': '}',
}


def find_invalid_char(line):
    stack = []
    for c in line:
        if c in openings:
            stack.append(openings[c])
        elif stack[-1] == c:
            stack.pop()
        else:
            return c

    return None

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

def get_all_points():
    for line in lines:
        c = find_invalid_char(line)
        if c is not None:
            yield points[c]

print(sum(get_all_points()))