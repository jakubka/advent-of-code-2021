with open("input_small2.txt", "r") as input_file:
    lines = input_file.read().strip().split("\n")

grid = [[int(d) for d in line] for line in lines]
grid_size = len(grid)
max_index = grid_size - 1

memoized_expenses = {(max_index, max_index): grid[max_index][max_index]}


def get_best_nei(x, y):
    def get_memoized_expense(x, y):
        if x < 0 or x == grid_size:
            return 9999999
        if y < 0 or y == grid_size:
            return 9999999
        point = (x, y)
        return memoized_expenses.get(point, 9999999)

    return min(
        [
            get_memoized_expense(x + 1, y),
            get_memoized_expense(x, y + 1),
            get_memoized_expense(x - 1, y),
            get_memoized_expense(x, y - 1),
        ]
    )


for x in range(grid_size - 1, -1, -1):
    for y in range(grid_size - 1, -1, -1):
        if x == max_index and y == max_index:
            continue
        expense = grid[y][x]
        best = get_best_nei(x, y)
        memoized_expenses[(x, y)] = best + expense

# print(memoized_expenses)

def draw_memo():
    for y in range(grid_size):
        for x in range(grid_size):
            print(str(memoized_expenses[(x, y)]).ljust(3, ' '), end="")
        print()
    print()

def draw_grid():
    for y in range(grid_size):
        for x in range(grid_size):
            print(str(grid[y][x]).ljust(3, ' '), end="")
        print()
    print()

draw_grid()
draw_memo()

print(memoized_expenses[(0, 0)] - grid[0][0])