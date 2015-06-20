import unittest
from parentheses import *

class TestParentheses(unittest.TestCase):
    def test_empty(self):
        # Arrange
        empty_parentheses = ""
        # Act
        answer = correct(empty_parentheses)
        # Assert
        self.assertTrue(answer)

    def test_correct_single_nesting(self):
        # Arrange
        correct_parentheses = "(())"
        # Act
        answer = correct(correct_parentheses)
        # Assert
        self.assertTrue(correct)

    def test_correct_multiple_nesting(self):
        # Arrange
        correct_parentheses = "(()())"
        # Act
        answer = correct(correct_parentheses)
        # Assert
        self.assertTrue(correct)

    def test_incorrect_eq_open_close(self):
        # Arrange
        incorrect_parentheses = "))(("
        # Act
        answer = correct(incorrect_parentheses)
        # Assert
        self.assertFalse(answer)

    def test_incorrect_uneq_open_close(self):
        # Arrange
        incorrect_parentheses = "((()())"
        # Act
        answer = correct(incorrect_parentheses)
        # Assert
        self.assertFalse(answer)

    def test_is_opening_true(self):
        # Arrange
        open_parenthesis = "("
        # Act
        answer = is_opening(open_parenthesis)
        # Assert
        self.assertTrue(answer)

    def test_is_opening_false(self):
        # Arrange
        close_parenthesis = ")"
        # Act
        answer = is_opening(close_parenthesis)
        # Assert
        self.assertFalse(answer)

if __name__ == '__main__':
    unittest.main()
