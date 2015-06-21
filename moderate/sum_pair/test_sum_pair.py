import unittest
from sum_pair import *

class TestSumPair(unittest.TestCase):
    def test_no_pair(self):
        # Arrange
        array = [1, 2, 3, 4]
        sum = 10
        # Act
        answer = sum_pair(array, sum)
        # Assert
        self.assertEquals(answer, [])

    def test_one_pair(self):
        # Arrange
        array = [10, 2, 3, 1]
        sum = 5
        # Act
        answer = sum_pair(array, sum)
        # Assert
        self.assertEquals(answer, [[2, 3]])

    def test_two_pairs(self):
        # Arrange
        array = [4, 3, 1, 2, 5, 6]
        sum = 5
        # Act
        answer = sum_pair(array, sum)
        # Assert
        self.assertEquals(answer, [[1, 4], [2, 3]])

if __name__ == '__main__':
    unittest.main()
