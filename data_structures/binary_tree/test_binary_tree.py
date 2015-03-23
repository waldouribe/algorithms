import unittest
from binary_tree import *

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.binary_tree = BinaryTree()

    def test_element_count(self):
        # Arrange
        binary_tree = self.binary_tree
        binary_tree.insert(1)
        binary_tree.insert(2)
        binary_tree.insert(3)
        # Act
        element_count = binary_tree.element_count()
        # Assert
        self.assertEqual(element_count, 3)

    def test_lookup_hit(self):
        # Arrange
        binary_tree = self.binary_tree
        binary_tree.insert(5)
        binary_tree.insert(3)
        binary_tree.insert(4)
        binary_tree.insert(7)
        # Act
        lookup_seven = binary_tree.lookup(7)
        # Assert
        self.assertTrue(lookup_seven)

    def test_lookup_miss(self):
        # Arrange
        binary_tree = self.binary_tree
        binary_tree.insert(5)
        binary_tree.insert(3)
        binary_tree.insert(4)
        binary_tree.insert(7)
        # Act
        lookup_seven = binary_tree.lookup(8)
        # Assert
        self.assertFalse(lookup_seven)

if __name__ == '__main__':
    unittest.main()
