import unittest
from my_set import *

class TestMySet(unittest.TestCase):
    def test_eq(self):
        # Arrange
        set1 = MySet()
        set2 = MySet()
        set1.insert(1)
        set1.insert(2)
        set2.insert(2)
        set2.insert(1)
        # Act
        answer = (set1 == set2)
        # Assert
        self.assertTrue(answer)

if __name__ == '__main__':
    unittest.main()
