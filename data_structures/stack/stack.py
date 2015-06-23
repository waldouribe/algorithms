class Stack:
    def __init__(self):
        self.array = []

    def push(self, value):
        self.array.append(value)
        return self

    def pop(self):
        return self.array.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.array[-1]

    def is_empty(self):
        return len(self.array) == 0

    def __eq__(self, other):
        return self.array == other.array

    def __str__(self):
        string = " | ".join( [ str(element) for element in self.array ] )
        return  "[ " + string

    def __repr__(self):
        return self.__str__()

    def sort(self):
        sorted_stack = Stack()
        while not self.is_empty():
            element_to_move = self.pop()
            while not(sorted_stack.is_empty()) and element_to_move > sorted_stack.peek():
                self.push(sorted_stack.pop())
            sorted_stack.push(element_to_move)
        self.array = sorted_stack.array
