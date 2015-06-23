import unittest
from stack import *

class TestStack(unittest.TestCase):
    def test_sort_empty(self):
        # Arrange
        stack = Stack()
        sorted_stack = Stack()
        # Act
        stack.sort
        # Assert
        self.assertEqual(stack, sorted_stack)

    def test_sort_inverted(self):
        # Arrange
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        sorted_stack = Stack()
        sorted_stack.push(3)
        sorted_stack.push(2)
        sorted_stack.push(1)
        # Act
        stack.sort()
        # Assert
        self.assertEqual(stack, sorted_stack)

    def test_sort_unsorted(self):
        # Arrange
        stack = Stack()
        stack.push(4)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        sorted_stack = Stack()
        sorted_stack.push(4)
        sorted_stack.push(3)
        sorted_stack.push(2)
        sorted_stack.push(1)
        # Act
        stack.sort()
        # Assert
        self.assertEqual(stack, sorted_stack)

if __name__ == '__main__':
    unittest.main()