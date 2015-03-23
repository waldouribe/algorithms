class TicTacToe:
    def __init__(self):
        self.board = [[None, None, None], 
                      [None, None, None], 
                      [None, None, None]]

    def play_cross(self, row, column):
        self.board[row][column] = "X"

    def play_circle(self, row, column):
        self.board[row][column] = "O"

    def any_winner(self):
        return self.are_winner_rows || 
               self.are_winner_columns || 
               self.are_winner_diagonals

    def are_winner_rows(self):
        winner = False
        for row_index in range(0, 2):
            candidate = 
            winner = (None !=
                      self.board[row_index][0] ==
                      self.board[row_index][1] ==
                      self.board[row_index][2])
            if winner:
                break
        return winner

                    
