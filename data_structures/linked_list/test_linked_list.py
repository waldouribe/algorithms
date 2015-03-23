import unittest
from linked_list import *

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.l = LinkedList()

    def test_first(self):
        # Arrange
        l = self.l
        # Act
        l.append(3)
        value = l.first()
        # Assert
        self.assertEqual(value, 3)

    def test_last(self):
        # Arrange
        l = self.l
        # Act
        l.append(3)
        l.append(5)
        value = l.last()
        # Assert
        self.assertEqual(value, 5)

    def test_lookup_hit(self):
        # Arrange
        l = self.l
        # Act
        l.append(3)
        l.append(5)
        lookup_answer = l.lookup(5)
        # Assert
        self.assertTrue(lookup_answer)

    def test_lookup_miss(self):
        # Arrange
        l = self.l
        # Act
        l.append(3)
        l.append(5)
        lookup_answer = l.lookup(4)
        # Assert
        self.assertFalse(lookup_answer)

if __name__ == '__main__':
    unittest.main()
