import unittest
from largest_sum import *

class TestLargestSum(unittest.TestCase):
    def test_greater_at_end(self):
        # Arrange
        array = [1, -1, 2]
        # Act
        answer = largest_sum(array)
        # Assert
        self.assertEquals(answer, 2)

    def test_two_seq_same_result(self):
        # Arrange
        array = [5, -3, 2, -3, 2, 5]
        # Act
        answer = largest_sum(array)
        # Assert
        self.assertEquals(answer, 8)

if __name__ == '__main__':
    unittest.main()