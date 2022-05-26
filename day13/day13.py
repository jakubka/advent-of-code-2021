with open("input.txt", "r") as input_file:
    lines = input_file.read().strip().split("\n")

points = [(int(x), int(y)) for x, y in (l.split(',') for l in lines if ',' in l)]

max_x = max(x for x, _ in points)
max_y = max(y for _, y in points)

grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

def print_grid():
    dots = 0

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print(grid[y][x], end='')
            if grid[y][x] == '#':
                dots += 1
        print()
    print()
    return dots

for x, y in points:
    grid[y][x] = '#'

def fold_y(fold_axis):
    global max_y
    for y in range(fold_axis):
        for x in range(max_x + 1):
            if grid[max_y - y][x] == '#':
                grid[y][x] = grid[max_y - y][x]
    max_y = fold_axis - 1

def fold_x(fold_axis):
    global max_x
    for x in range(fold_axis):
        for y in range(max_y + 1):
            if grid[y][max_x - x] == '#':
                grid[y][x] = grid[y][max_x - x]
    max_x = fold_axis - 1

fold_x(655)
fold_y(447)
fold_x(327)
fold_y(223)
fold_x(163)
fold_y(111)
fold_x(81)
fold_y(55)
fold_x(40)
fold_y(27)
fold_y(13)
fold_y(6)
dots = print_grid()
print(f'Dots: ${dots}')

# HEJHJRCJ