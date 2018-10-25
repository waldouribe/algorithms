import unittest
from methods import * 

class TestBinarySearch(unittest.TestCase):
    def test_singleton(self):
        needle = 'a'
        haystack = ['a']
        answer = binary_search(needle, haystack)
        self.assertEqual(answer, 0)

    def test_rightmost(self):
        needle = 'c'
        haystack = ['a', 'b', 'c']
        answer = binary_search(needle, haystack)
        self.assertEqual(answer, 2)

    def test_leftmost(self):
        needle = 'a'
        haystack = ['a', 'b', 'c']
        answer = binary_search(needle, haystack)
        self.assertEqual(answer, 0)

    def test_inbetween(self):
        needle = 'c'
        haystack = ['a', 'b', 'c', 'd', 'e']
        answer = binary_search(needle, haystack)
        self.assertEqual(answer, 2)

    def test_not_found(self):
        needle = 'z'
        haystack = ['a', 'b', 'c', 'd', 'e']
        answer = binary_search(needle, haystack)
        self.assertEqual(answer, -1)

if __name__ == '__main__':
    unittest.main()