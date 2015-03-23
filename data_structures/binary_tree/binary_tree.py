from node import *

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self.insert_recursive(value, self.root)
        return self

    def insert_recursive(self, value, node):
        if node is None:
            return Node(value)
        else:
            if value < node.value:
                return node.insert_left(self.insert_recursive(value, node.left))
            else:
                return node.insert_right(self.insert_recursive(value, node.right))

    def lookup(self, value):
        return self.search(value) is not None

    def element_count(self):
        return self.element_count_recursive(self.root)

    def element_count_recursive(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.element_count_recursive(node.left) + self.element_count_recursive(node.right)

    def search(self, value):
        return self.search_recursive(value, self.root)

    def search_recursive(self, value, node):
        if node is None:
            return None
        else:
            if node.value == value:
                return node
            elif value < node.value:
                return self.search_recursive(value, node.left)
            else:
                return self.search_recursive(value, node.right)
