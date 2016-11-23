import unittest
from keyword_builder import *

class TestKeywords(unittest.TestCase):
    def test_equilibrium(self):
        # Arrange
        a = [-1, 3, -4, 5, 1, -6, 2, 1]
        # Act
        answer = equilibrium(a)
        # Assert
        self.assertEqual(answer, 1)

if __name__ == '__main__':
    meta_keyword = MetaKeyword('comprar', [], True, 1)
    print(MetaKeyword.generate_keywords([meta_keyword]))

