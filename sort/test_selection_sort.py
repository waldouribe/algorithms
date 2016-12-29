import unittest
from methods import *

class TestSelectionSort(unittest.TestCase):
    def test_empty_array(self):
        a = []
        answer = selection_sort(a)
        self.assertEquals(answer, [])

    def test_ordered_array(self):
        a = [1, 2, 3, 4]
        answer = selection_sort(a)
        self.assertEquals(answer, [1, 2, 3, 4])

    def test_inverted_array(self):
        a = [4, 3, 2, 1]
        answer = selection_sort(a)
        self.assertEquals(answer, [1, 2, 3, 4])

    def test_one_out_of_order_array(self):
        a = [1, 3, 2, 4]
        answer = selection_sort(a)
        self.assertEquals(answer, [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()