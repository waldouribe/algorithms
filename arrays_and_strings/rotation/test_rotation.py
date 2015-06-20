import unittest
from rotation import *

class TestRotation(unittest.TestCase):
    def test_01(self):
        # Arrange
        s_1 = "rosa"
        s_2 = "saro"
        # Act
        answer = rotation(s_1, s_2)
        # Assert
        self.assertTrue(answer)

    def test_02(self):
        # Arrange
        s_1 = "rosamel"
        s_2 = "fierro"
        # Act
        answer = rotation(s_1, s_2)
        # Assert
        self.assertFalse(answer)

    def test_03(self):
        # Arrange
        s_1 = "rosa"
        s_2 = "sroa"
        # Act
        answer = rotation(s_1, s_2)
        # Assert
        self.assertFalse(answer)

    def test_04(self):
        # Arrange
        s_1 = "rosa"
        s_2 = "aros"
        # Act
        answer = rotation(s_1, s_2)
        # Assert
        self.assertTrue(answer)

    def test_05(self):
        # Arrange
        s_1 = "rosa"
        s_2 = "ar"
        # Act
        answer = rotation(s_1, s_2)
        # Assert
        self.assertFalse(answer)

    def test_06(self):
        # Arrange
        s_1 = "rossa"
        s_2 = "ssaro"
        # Act
        answer = rotation(s_1, s_2)
        # Assert
        self.assertTrue(answer)

    def test_07(self):
        # Arrange
        s_1 = "ssrao"
        s_2 = "rossa"
        # Act
        answer = rotation(s_1, s_2)
        # Assert
        self.assertFalse(answer)

if __name__ == '__main__':
    unittest.main()
