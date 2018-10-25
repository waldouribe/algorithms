import unittest
from methods import *

class TestQuickSort(unittest.TestCase):
    def test_partition_singleton(self):
        a = [1]
        answer = partition(a, 0, len(a)-1)        
        self.assertEquals(answer, 0)

    def test_partition_center(self):
        a = [0, 1, 5, 4, 3]
        answer = partition(a, 0, len(a)-1)
        self.assertEquals(answer, 2)

    def test_partition_left(self):
        a = [1, 2, 6, 3, 8]
        answer = partition(a, 0, len(a)-1)
        self.assertEquals(answer, 4)

    def test_partition_left_two_elements(self):
        a = [2, 1]
        answer = partition(a, 0, len(a)-1)
        self.assertEquals(answer, 0)

    def test_partition_right_two_elements(self):
        a = [4, 5]
        answer = partition(a, 0, len(a)-1)
        self.assertEquals(answer, 1)

    def test_empty_array(self):
        a = []
        answer = quicksort(a)
        self.assertEquals(a, [])

    def test_ordered_array(self):
        a = [1, 2, 3, 4]
        answer = quicksort(a)
        self.assertEquals(a, [1, 2, 3, 4])

    def test_inverted_array(self):
        a = [4, 3, 2, 1]
        answer = quicksort(a)
        self.assertEquals(a, [1, 2, 3, 4])

    def test_one_out_of_order_array(self):
        a = [1, 3, 2, 4]
        answer = quicksort(a)
        self.assertEquals(a, [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
