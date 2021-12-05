import sys

class BingoBoard:

    def __init__(self, values):
        self.board = values
        self.tracker_board = self.build_tracker_board()

    def build_tracker_board(self):
        self.row_len = len(self.board)
        self.col_len = len(self.board[0])
        tracker_board = []
        for _ in range(self.row_len):
            tracker_board.append([0 for _ in range(self.col_len)])
        return tracker_board

    def _board_index(self, number):
        for i, row in enumerate(self.board):
            if number in row:
                return i, row.index(number)
        return -1, -1

    def mark_tracker_board(self, number):
        row_index, col_index = self._board_index(number)
        if row_index != -1:
            self.tracker_board[row_index][col_index] = 1

    def check_if_won(self):
        for i, row in enumerate(self.tracker_board):
            if sum(row) == self.row_len:
                return True
            
        for i in range(self.col_len):
            colsum = sum(row[i] for row in self.tracker_board)
            if colsum == self.col_len:
                return True
        return False

    def sum_unmarked_board_values(self):
        sum = 0
        for r in range(self.row_len):
            for c in range(self.col_len):
                if self.tracker_board[r][c] == 0:
                    sum+=self.board[r][c]
        return sum

if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        input = f.read().splitlines()

    number_draws = input[0].strip().split(',')
    board_values = input[2:]

    bingo_boards = []
    values = []

    for i, row in enumerate(board_values):
        if row == '':
            if len(values) > 0:
                bingo_boards.append(BingoBoard(values))
            values = []
            continue
        values.append([int(x) for x in row.split()])
    
    for num in number_draws:
        for board in bingo_boards:
            board.mark_tracker_board(int(num))
            won = board.check_if_won()
            if won:
                unmarked_sum = board.sum_unmarked_board_values()
                print(unmarked_sum * int(num))
                sys.exit()
                

