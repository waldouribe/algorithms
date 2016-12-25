import numpy as np


class Tictactoe:
    X_VALUE = -1
    O_VALUE = 1

    def __init__(self):
        self.matrix = np.matrix('0 0 0; 0 0 0; 0 0 0')#[[0 for x in range(size)] for y in range(size)]

    def x(self, row, column):
        self.matrix[row, column] = self.X_VALUE

    def o(self, row, column):
        self.matrix[row, column] = self.O_VALUE

    def any_winner(self):
        row_sums = np.sum(self.matrix, axis=1)
        for row_sum in row_sums:
            if 3 in row_sum or -3 in row_sum:
                return True

        col_sums = np.sum(self.matrix, axis=0)
        for col_sum in col_sums:
            if 3 in col_sum or -3 in col_sum:
                return True


        diagonal_left_right = abs(self.matrix.item(0,0) + self.matrix.item(1,1) + self.matrix.item(2,2))
        diagonal_right_left = abs(self.matrix.item(0,2) + self.matrix.item(1,1) + self.matrix.item(2,0))
        if diagonal_left_right == 3 or diagonal_right_left == 3:
            return True

        return False 

