class Board:
    def __init__(self, number_rows):
        self.number_rows = number_rows

    def mark_number(self, number_to_mark):
        for row in self.number_rows:
            for i, n in enumerate(row):
                if n == number_to_mark:
                    row[i] = None

    def check_win_condition(self):
        for row in self.number_rows:
            if all(n == None for n in row):
                return True

        for i in range(0, len(self.number_rows[0])):
            if all(row[i] == None for row in self.number_rows):
                return True

        return False

    def get_sum_of_unmarked_numbers(self):
        return sum(n for row in self.number_rows for n in row if n is not None)

    def print_board(self):
        for row in self.number_rows:
            for n in row:
                print(n if n is not None else "__", end=" ")
            print()

with open("input.txt", "r") as input_file:
    lines = input_file.read().split("\n")

drawn_numbers = [int(n) for n in lines[0].split(",")]
boards = []
for board_start_index in range(2, len(lines), 6):
    sliced_lines = lines[board_start_index : (board_start_index + 5)]
    number_rows = [[int(n) for n in line.split()] for line in sliced_lines]
    board = Board(number_rows)
    boards.append(board)

for n in drawn_numbers:
    for board in boards:
        board.mark_number(n)
        if board.check_win_condition():
            print('Great job, you beat the giant squid! 🎉')
            print(board.get_sum_of_unmarked_numbers() * n)
            exit()