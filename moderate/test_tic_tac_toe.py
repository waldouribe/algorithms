import unittest
from tic_tac_toe import *

class TestTicTacToe(unittest.TestCase):
    def test_win_line(self):
        # Arrange
        t = TicTacToe()
        t.play_cross(0, 0)
        t.play_cross(0, 1)
        t.play_cross(0, 2)
        # Act
        answer = t.any_winner()
        # Assert
        self.assertTrue(answer)

    def test_deuce_line(self):
        # Arrange
        t = TicTacToe()
        t.play_cross(0, 0)
        t.play_circle(0, 1)
        t.play_cross(0, 2)
        # Act
        answer = t.any_winner()
        # Assert
        self.assertFalse(answer)


if __name__ == '__main__':
    unittest.main()
