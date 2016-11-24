# encoding: utf-8
class MetaKeyword:
    def __init__(self, word, required, position):
        self.word = word
        self.required = required
        self.position = position

    @staticmethod
    def generate_keywords(meta_keywords):
        keywords = []
        required = []
        optional = []
        
        for meta_keyword in meta_keywords:
            if meta_keyword.required:
                required.append(meta_keyword)
            else:
                optional.append(meta_keyword)

        
        keywords.append(' '.join(map(lambda mk: mk.word, required)))

        
        for pivot in range(0, len(optional)):
            for i in range(pivot, len(optional)):
                keyword = ' '.join(map(lambda mk: mk.word, sorted(optional[pivot:i+1] + required, key=lambda mk: mk.position)))
                keywords.append(keyword)
        return keywords

