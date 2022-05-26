with open("input.txt", "r") as input_file:
    lines = input_file.read().strip().split("\n")

grid = [[int(d) for d in line] for line in lines]

grid_size = len(grid)
max_expense = 999999999
predicted_avg_expense = 3

# visited_coords = set()


def draw_path(visited_points_set):
    visited_grid = [["_" for __ in range(grid_size)] for _ in range(grid_size)]
    for x, y in visited_points_set:
        visited_grid[y][x] = "X"
    return "\n".join("".join(row) for row in visited_grid)


def can_visit(x, y, visited_coords_set):
    if x < 0 or x == grid_size:
        return False
    if y < 0 or y == grid_size:
        return False
    if (x, y) in visited_coords_set:
        return False

    return True


def get_approx_expense_towards_the_end(x, y):
    remaining_steps = (grid_size - x - 1) + (grid_size - y - 1)
    if remaining_steps < 5:
        return 0
    return remaining_steps * (predicted_avg_expense - 0.5)


number_of_visits = 0
min_expense_so_far = (grid_size - 1) * 2 * predicted_avg_expense


def explore(x, y, expense_so_far, visited_coords_set):
    global number_of_visits, min_expense_so_far
    number_of_visits += 1
    if number_of_visits % 10000 == 0:
        print(number_of_visits)
    # print(f"Exploring: {(x, y)}, path so far: {path}")
    new_expense_so_far = expense_so_far + grid[y][x] if x != 0 or y != 0 else 0
    if new_expense_so_far >= min_expense_so_far:
        # print(
        #     f"Ending early, expense is already {new_expense_so_far}, but we already have path with {min_expense_so_far}"
        # )
        return max_expense
    approx_remaining_expense = get_approx_expense_towards_the_end(x, y)
    if new_expense_so_far + approx_remaining_expense >= min_expense_so_far:
        # print(
        #     f"Ending early, expense is already {new_expense_so_far}, approx more {approx_remaining_expense}, but we already have path with {min_expense_so_far}"
        # )
        return max_expense
    new_visited_coords = visited_coords_set.union([(x, y)])
    if x == grid_size - 1 and y == grid_size - 1:
        print(f"Reached end: {(x, y)}, expense: {new_expense_so_far}")
        print(draw_path(new_visited_coords))
        return new_expense_so_far
    possible_paths = [
        # right
        explore(x + 1, y, new_expense_so_far, new_visited_coords)
        if can_visit(x + 1, y, visited_coords_set)
        else max_expense,
        # down
        explore(x, y + 1, new_expense_so_far, new_visited_coords)
        if can_visit(x, y + 1, visited_coords_set)
        else max_expense,
        # left
        explore(x - 1, y, new_expense_so_far, new_visited_coords)
        if can_visit(x - 1, y, visited_coords_set)
        else max_expense,
        # top
        explore(x, y - 1, new_expense_so_far, new_visited_coords)
        if can_visit(x, y - 1, visited_coords_set)
        else max_expense,
    ]
    expense = min(possible_paths)
    if expense < min_expense_so_far:
        min_expense_so_far = expense
    return expense


# print(grid)
# print(len(grid))
# print(len(grid[0]))
print(explore(0, 0, 0, set()))
print(f"Visits: {number_of_visits}")



