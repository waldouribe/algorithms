import unittest
from tictactoe import *

class TestTictactoe(unittest.TestCase):
    def test_no_winners(self):
        # Arrange
        t = Tictactoe()
        t.o(0, 0)
        t.o(0, 1)
        t.x(0, 2)
        # Act
        answer = t.any_winner()
        # Assert
        self.assertEquals(answer, False)

    def test_o_row_winner(self):
        # Arrange
        t = Tictactoe()
        t.x(0, 0)
        t.x(0, 1)
        t.o(0, 2)
        t.o(1, 0)
        t.o(1, 1)
        t.o(1, 2)
        # Act
        answer = t.any_winner()
        # Assert
        self.assertEquals(answer, True)

    def test_x_row_winner(self):
        # Arrange
        t = Tictactoe()
        t.x(0, 0)
        t.x(0, 1)
        t.o(0, 2)
        t.x(1, 0)
        t.x(1, 1)
        t.x(1, 2)
        # Act
        answer = t.any_winner()
        # Assert
        self.assertEquals(answer, True)

    def test_x_col_winner(self):
        # Arrange
        t = Tictactoe()
        t.x(0, 0)
        t.x(1, 0)
        t.x(2, 0)
        # Act
        answer = t.any_winner()
        # Assert
        self.assertEquals(answer, True)

    # def test_one_pair(self):
    #     # Arrange
    #     array = [10, 2, 3, 1]
    #     sum = 5
    #     # Act
    #     answer = sum_pair(array, sum)
    #     # Assert
    #     self.assertEquals(answer, [[2, 3]])

    # def test_two_pairs(self):
    #     # Arrange
    #     array = [4, 3, 1, 2, 5, 6]
    #     sum = 5
    #     # Act
    #     answer = sum_pair(array, sum)
    #     # Assert
    #     self.assertEquals(answer, [[1, 4], [2, 3]])

if __name__ == '__main__':
    unittest.main()
