from node import *

class LinkedList:
    def __init__(self):
        self.root = None

    def append(self, value):
        self.root = self.append_recursive(value, self.root)

    def append_recursive(self, value, node):
        if node is None:
            return Node(value)
        else:
            return self.append_recursive(value, node.next)

    def lookup(self, value):
        return self.lookup_recursive(value, self.root)

    def lookup_recursive(self, value, node):
        if node is None:
            return False
        else:
            if node.value == value:
                return True
            else:
                return self.lookup_recursive(value, node.next)

    def first(self):
        root = self.root

        if root is None:
            return None
        else:
            return root.value

    def last(self):
        return self.last_recursive(self.root)

    def last_recursive(self, node):
        if node is None:
            return None
        elif node.next is None:
            return node.value
        else:
            return self.last_recursive(node.next)
