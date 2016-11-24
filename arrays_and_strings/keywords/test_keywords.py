import unittest
from meta_keyword import *

class TestKeywords(unittest.TestCase):
    def test_one_required(self):
        # Arrange
        meta_keyword = MetaKeyword('comprar', True, 1)
        # Act
        answer = MetaKeyword.generate_keywords([meta_keyword])
        # Assert
        self.assertEqual(answer, ['comprar'])

    def test_two_required(self):
        # Arrange        
        meta_keywords = []
        meta_keywords.append(MetaKeyword('comprar', True, 1))
        meta_keywords.append(MetaKeyword('gopro', True, 2))
        # Act
        answer = MetaKeyword.generate_keywords(meta_keywords)
        # Assert
        self.assertEqual(answer, ['comprar gopro'])

    def test_two_required_one_optional(self):
        # Arrange        
        meta_keywords = []
        meta_keywords.append(MetaKeyword('comprar', True, 1))
        meta_keywords.append(MetaKeyword('gopro', True, 2))
        meta_keywords.append(MetaKeyword('santiago', False, 3))
        # Act
        answer = MetaKeyword.generate_keywords(meta_keywords)
        # Assert
        self.assertEqual(answer, ['comprar gopro', 'comprar gopro santiago'])

    def test_two_required_two_optional(self):
        # Arrange        
        meta_keywords = []
        meta_keywords.append(MetaKeyword('comprar', True, 1))
        meta_keywords.append(MetaKeyword('gopro', True, 2))
        meta_keywords.append(MetaKeyword('santiago', False, 3))
        meta_keywords.append(MetaKeyword('las condes', False, 4))
        # Act
        answer = MetaKeyword.generate_keywords(meta_keywords)
        # Assert
        self.assertEqual(answer, ['comprar gopro', 'comprar gopro santiago', 'comprar gopro santiago las condes', 'comprar gopro las condes'])

    def test_one_required_two_optional_one_required(self):
        # Arrange        
        meta_keywords = []
        meta_keywords.append(MetaKeyword('gopro', True, 2))
        meta_keywords.append(MetaKeyword('santiago', False, 3))
        meta_keywords.append(MetaKeyword('las condes', False, 4))
        meta_keywords.append(MetaKeyword('en oferta', True, 5))
        # Act
        answer = MetaKeyword.generate_keywords(meta_keywords)
        # Assert
        self.assertEqual(answer, ['gopro en oferta', 'gopro santiago en oferta', 'gopro santiago las condes en oferta', 'gopro las condes en oferta'])

if __name__ == '__main__':
    unittest.main()
