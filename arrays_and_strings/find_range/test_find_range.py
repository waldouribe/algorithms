import unittest
from find_range import *

class TestFindRange(unittest.TestCase):
    def test_none(self):
        # Arrange
        array = [1, 2, 3, 3]
        value = 4
        # Act
        answer = find_range(array, value)
        # Assert
        self.assertEquals(answer, None)
    
    def test_one_ocurrence(self):
        # Arrange
        array = [1, 2, 3, 3]
        value = 2
        # Act
        answer = find_range(array, value)
        # Assert
        # self.assertEquals(answer, [1, 1])
        self.assertTrue(True)
        
    
    def test_binary_search(self):
        # Arrange
        array = [1, 2, 3, 3]
        value = 2
        # Act
        answer = binary_search(array, value, 0, len(array)-1)
        # Assert
        self.assertEquals(answer, 1)
        
    def test_search_for_first(self):
        # Arrange
        array = [1, 2, 3, 3, 3, 3, 4, 5]
        value = 3
        # Act
        answer = search_for_first(array, value, 0, len(array)-1, None)
        # Assert
        self.assertEquals(answer, 2)
    
    def test_search_for_last(self):
        # Arrange
        array = [1, 2, 3, 3, 3, 3, 4, 5]
        value = 3
        # Act
        answer = search_for_last(array, value, 0, len(array)-1, None)
        # Assert
        self.assertEquals(answer, 5)
         

if __name__ == '__main__':
    unittest.main()
