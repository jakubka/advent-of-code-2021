with open("input.txt", "r") as input_file:
    lines = input_file.read().strip().split("\n")

rows = [[int(i) for i in l] for l in lines]

total_risk = 0
for row_i, row in enumerate(rows):
    for col_i, number in enumerate(row):
        top = row_i == 0 or rows[row_i - 1][col_i] > number
        bottom = row_i == len(rows) - 1 or rows[row_i + 1][col_i] > number
        left = col_i == 0 or row[col_i - 1] > number
        right = (col_i == len(row) - 1) or row[col_i + 1] > number

        if top and bottom and left and right:
            total_risk += number + 1

print(total_risk)