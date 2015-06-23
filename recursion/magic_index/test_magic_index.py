import unittest
from magic_index import *

class TestMagicIndex(unittest.TestCase):
    def test_no_index(self):
        # Arrange
        array = [1, 2, 3, 4]
        # Act
        answer = magic_index(array)
        # Assert
        self.assertEquals(answer, -1)

    def test_one_index(self):
        # Arrange
        array = [1, 1, 3, 4]
        # Act
        answer = magic_index(array)
        # Assert
        self.assertEquals(answer, 1)

if __name__ == '__main__':
    unittest.main()
