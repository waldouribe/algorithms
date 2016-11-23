# encoding: utf-8
class MetaKeyword:
    def __init__(self, word, synonyms, required, position):
        self.word = word
        self.synonyms = synonyms
        self.required = required
        self.position = position

    @staticmethod
    def generate_keywords(meta_keywords):
        keywords = []
        for meta_keyword in meta_keywords:
            keywords.append(meta_keyword.word)
        return keywords



    