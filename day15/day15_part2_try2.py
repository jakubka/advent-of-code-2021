import heapq
from itertools import product

with open("input.txt", "r") as input_file:
    lines = input_file.read().strip().split("\n")


def create_small_grid():
    grid = [[int(d) for d in line] for line in lines]
    grid_size = len(grid)
    return grid, grid_size


def create_extended_grid():
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

    return grid, grid_size


grid, grid_size = create_extended_grid()
# grid, grid_size = create_small_grid()
max_index = grid_size - 1


def get_neighbours(x, y):
    def is_in_bounds(x, y):
        if x < 0 or x == grid_size:
            return False
        if y < 0 or y == grid_size:
            return False
        return True

    return [
        p
        for p in [
            (x + 1, y),
            (x, y + 1),
            (x - 1, y),
            (x, y - 1),
        ]
        if is_in_bounds(p[0], p[1])
    ]


def get_estimated_cost(x, y):
    return grid_size - 1 - x + grid_size - 1 - y


def run():
    points_to_visit = [(0, get_estimated_cost(0, 0), (0, 0))]
    visited_points = {(0, 0)}

    while len(points_to_visit) > 0:
        cost, _, (x, y) = heapq.heappop(points_to_visit)
        for dest_x, dest_y in get_neighbours(x, y):
            if dest_x == max_index and dest_y == max_index:
                return cost + grid[dest_y][dest_x]
            elif (dest_x, dest_y) not in visited_points:
                visited_points.add((dest_x, dest_y))
                heapq.heappush(
                    points_to_visit,
                    (
                        cost + grid[dest_y][dest_x],
                        get_estimated_cost(dest_x, dest_y),
                        (dest_x, dest_y),
                    ),
                )


print(run())


def draw_grid():
    for y in range(grid_size):
        for x in range(grid_size):
            print(grid[y][x], end="")
        print()
