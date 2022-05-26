with open("input_full.txt", "r") as input_file:
    lines = input_file.read().strip().split("\n")

rows = [[int(i) for i in l] for l in lines]

def mark_cell(row_i, col_i):
    number = rows[row_i][col_i]
    rows[row_i][col_i] = None
    size = 1
    # top
    if row_i != 0 and rows[row_i - 1][col_i] != 9 and rows[row_i - 1][col_i] != None and rows[row_i - 1][col_i] > number:
        size += mark_cell(row_i - 1, col_i)
    # bottom
    if row_i != len(rows) - 1 and rows[row_i + 1][col_i] != 9 and rows[row_i + 1][col_i] != None and rows[row_i + 1][col_i] > number:
        size += mark_cell(row_i + 1, col_i)
    # left
    if col_i != 0 and rows[row_i][col_i - 1] != 9 and rows[row_i][col_i - 1] != None and rows[row_i][col_i - 1] > number:
        size += mark_cell(row_i, col_i - 1)
    # right
    if col_i != len(rows[0]) -1 and rows[row_i][col_i + 1] != 9 and rows[row_i][col_i + 1] != None and rows[row_i][col_i + 1] > number:
        size += mark_cell(row_i, col_i + 1)

    return size

all_basins = []
for row_i, row in enumerate(rows):
    for col_i, number in enumerate(row):
        if number is None:
            continue
        top = row_i == 0 or (rows[row_i - 1][col_i] != None and rows[row_i - 1][col_i] > number)
        bottom = row_i == len(rows) - 1 or (rows[row_i + 1][col_i] != None and rows[row_i + 1][col_i] > number)
        left = col_i == 0 or (row[col_i - 1] != None and row[col_i - 1] > number)
        right = (col_i == len(row) - 1) or (row[col_i + 1] != None and row[col_i + 1] > number)

        if top and bottom and left and right:
            all_basins.append(mark_cell(row_i, col_i))
            # print(rows)

all_basins.sort(reverse=True)

print(all_basins[0] * all_basins[1] * all_basins[2])