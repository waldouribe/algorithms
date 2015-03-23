class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def insert(self, value):
        self.next = Node(value)
        return self

    def __str__(self):
        return self.value + "->"