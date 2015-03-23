import unittest
from node import *

class TestNode(unittest.TestCase):
    def setUp(self):
        self.node = Node(1)

    def test_insert(self):
        # Arrange
        node = self.node
        # Act
        node.insert(2)
        value = node.next.value
        # Assert
        self.assertEqual(value, 2)

if __name__ == '__main__':
    unittest.main()