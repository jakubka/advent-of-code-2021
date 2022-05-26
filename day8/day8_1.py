with open("input.txt", "r") as input_file:
    lines = input_file.read().strip().split("\n")

def get_len(input_line):
    inputs = input_line.split("|")[1].split()
    result = len([input for input in inputs if len(input) in [2, 3, 4, 7]])
    return result

lens = (get_len(line) for line in lines)
print(sum(lens))