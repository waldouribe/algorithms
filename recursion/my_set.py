class MySet:
    def __init__(self):
        self.elements = []

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.elements)

    def insert(self, element):
        if not self.exists(element):
            self.elements.append(element)
        return self

    def exists(self, element):
        return element in self.elements

    def __eq__(self, another_set):
        return sorted(self.elements) == sorted(another_set.elements)

    def subsets(self):
        if self.empty:
            return MySet()
        elif (self.size() == 1):
            return [MySet(), self]
        else:
            
