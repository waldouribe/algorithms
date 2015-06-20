import unittest
from closest_pair import *

class TestClosestPair(unittest.TestCase):
    def test_closest_pair(self):
        # Arrange
        array = [10, 1, 20, 4, 12, 5]
        # Act
        answer = closest_pair(array)
        # Assert
        self.assertEquals(answer, [4, 5])

if __name__ == '__main__':
    unittest.main()