class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, a_node):
        self.left = a_node
        return self

    def insert_right(self, a_node):
        self.right = a_node
        return self