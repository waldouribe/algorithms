import unittest
from my_string import *

class TestMyString(unittest.TestCase):
    def test_unique_true(self):
        # Arrange
        s = MyString("abcde")
        # Act
        answer = s.all_unique_chars()
        # Assert
        self.assertTrue(answer)

    def test_rotation_true(self):
        # Arrange
        s = MyString("rosa")
        # Act
        answer = s.all_unique_chars()
        # Assert
        self.assertTrue(answer)

    def test_unique_false(self):
        # Arrange
        s = MyString("abccde")
        # Act
        answer = s.all_unique_chars()
        # Assert
        self.assertFalse(answer)

    def test_anagram_false(self):
        # Arrange
        s = MyString("hola")
        # Act
        answer = s.anagram("chao")
        # Assert
        self.assertFalse(answer)

    def test_anagram_true(self):
        # Arrange
        s = MyString("amor")
        # Act
        answer = s.anagram("roma")
        # Assert
        self.assertTrue(answer)

if __name__ == '__main__':
    unittest.main()
