import unittest
from my_max import *

class TestMyMax(unittest.TestCase):
    def test_max(self):
        # Arrange
        x = 2
        y = 10
        # Act
        answer = my_max(x, y)
        # Assert
        self.assertEquals(answer, y)

if __name__ == '__main__':
    unittest.main()