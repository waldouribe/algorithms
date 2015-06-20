import unittest
from my_max import *

class TestSumPair(unittest.TestCase):
    def test_no_pair(self):
        # Arrange
        array = [1, 2, 3, 4]
        sum = [10]
        # Act
        answer = sum_pair(array, sum)
        # Assert
        self.assertEquals(answer, [])

if __name__ == '__main__':
    unittest.main()