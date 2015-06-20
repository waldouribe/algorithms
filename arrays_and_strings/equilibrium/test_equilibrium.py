import unittest
from equilibrium import *

class TestEquilibrium(unittest.TestCase):
    def test_equilibrium(self):
        # Arrange
        a = [-1, 3, -4, 5, 1, -6, 2, 1]
        # Act
        answer = equilibrium(a)
        # Assert
        self.assertEqual(answer, 1)

if __name__ == '__main__':
    unittest.main()
