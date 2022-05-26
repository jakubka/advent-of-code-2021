from itertools import product

with open("input.txt", "r") as input_file:
    lines = input_file.read().strip().split("\n")

# grid = [[int(d) for d in line] for line in lines]
# grid_size = len(grid)

small_grid = [[int(d) for d in line] for line in lines]
small_grid_size = len(small_grid)

grid_size = small_grid_size * 5
grid = [[None for __ in range(grid_size)] for _ in range(grid_size)]

for x, y in product(range(small_grid_size), range(small_grid_size)):
    grid[y][x] = small_grid[y][x]


def next_number(i):
    return 1 if i == 9 else i + 1


for x in range(small_grid_size, grid_size):
    for y in range(small_grid_size):
        grid[y][x] = next_number(grid[y][x - small_grid_size])

for x in range(grid_size):
    for y in range(small_grid_size, grid_size):
        grid[y][x] = next_number(grid[y - small_grid_size][x])

max_index = grid_size - 1

memoized_expenses = {(max_index, max_index): (grid[max_index][max_index], 1)}


def get_nearby_memoized_expenses(x, y):
    def get_memoized_expense(x, y):
        if x < 0 or x == grid_size:
            return False
        if y < 0 or y == grid_size:
            return False
        point = (x, y)
        return memoized_expenses.get(point, False)

    return [
        p
        for p in [
            get_memoized_expense(x + 1, y),
            get_memoized_expense(x, y + 1),
            get_memoized_expense(x - 1, y),
            get_memoized_expense(x, y - 1),
        ]
        if p
    ]


def get_best_nei(x, y):
    return min(get_nearby_memoized_expenses(x, y), key=lambda x: x[0])


def run():
    for x in range(grid_size - 1, -1, -1):
        for y in range(grid_size - 1, -1, -1):
            if x == max_index and y == max_index:
                continue
            expense = grid[y][x]
            best_expense, steps = get_best_nei(x, y)
            memoized_expenses[(x, y)] = (best_expense + expense, steps + 1)


def fix_problematic_points():
    fixed = 0
    for y in range(grid_size):
        for x in range(grid_size):
            other_p = get_nearby_memoized_expenses(x, y)
            current_p = memoized_expenses[(x, y)]
            better_points = [
                p
                for p in other_p
                if (p[0] < current_p[0] and p[1] >= current_p[1])
                or (p[0] == current_p[0] and p[0] < current_p[1] - 1)
            ]
            if len(better_points) > 0:
                fixed += 1
                better_point = min(better_points)
                # if len(better_points) > 1:
                #     print(f"{len(better_points)} better points. {better_points}, using {better_point}")
                memoized_expenses[(x, y)] = (
                    better_point[0] + grid[y][x],
                    better_point[1] + 1,
                )

    return fixed


def fix_problematic_point(x, y):
    other_p = get_nearby_memoized_expenses(x, y)
    current_p = memoized_expenses[(x, y)]
    better_matches = [p for p in other_p if p[0] < current_p[0] and p[1] > current_p[1]]

    if len(better_matches) > 0:
        better_match = better_matches[0]
        memoized_expenses[(x, y)] = (better_match[0] + grid[y][x], better_match[1] + 1)


def fix_problematic(points):
    for x, y in points:
        fix_problematic_point(x, y)


def draw_memo():
    for y in range(grid_size):
        for x in range(grid_size):
            print(str(memoized_expenses[(x, y)]).rjust(9, " "), end="")
        print()
    print()


def draw_grid():
    for y in range(grid_size):
        for x in range(grid_size):
            print(grid[y][x], end="")
        print()


def draw_path(points):
    visited_grid = [["_" for __ in range(grid_size)] for _ in range(grid_size)]
    for x, y in points:
        visited_grid[y][x] = "X"
    g = "\n".join("".join(row) for row in visited_grid)
    print(g)
    print()


run()
# draw_grid()

# draw_memo()
print(memoized_expenses[(0, 0)][0] - grid[0][0])

while True:
    points_fixed = fix_problematic_points()
    print(f"Fixed {points_fixed} problems")
    # draw_memo()
    if points_fixed == 0:
        break

print(memoized_expenses[(0, 0)][0] - grid[0][0])
