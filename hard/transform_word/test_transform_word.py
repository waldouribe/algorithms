import unittest
from transform_word import *

class TestTransformWord(unittest.TestCase):
  def test_01(self):
    dictionary = ['damp', 'lamp', 'limp', 'lime', 'like', 'foo']
    word1 = 'damp'
    word2 = 'like'
    answer = transform_word(dictionary, word1, word2)
    self.assertEqual(answer, ['damp', 'lamp', 'limp', 'lime', 'like'])

if __name__ == '__main__':
  unittest.main()