import statistics

with open("input.txt", "r") as input_file:
    lines = input_file.read().strip().split("\n")

openings = {
    "(": ")",
    "[": "]",
    "<": ">",
    "{": "}",
}

score_dict = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def find_incomplete_score(line):
    stack = []
    for c in line:
        if c in openings:
            stack.append(openings[c])
        elif stack[-1] == c:
            stack.pop()
        else:
            return 0

    if len(stack) == 0:
        return 0

    stack.reverse()
    score = 0
    for c in stack:
        score *= 5
        score += score_dict[c]
    return score


points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

scores = [s for s in [find_incomplete_score(l) for l in lines] if s > 0]
print(scores)
print(statistics.median(scores))
