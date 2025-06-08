from ..base.preprocessor import BasePreprocessor

class SimpleTokenizer(BasePreprocessor):
    def process(self, text):
        return text.split() if isinstance(text, str) else []

def whitespace_tokenize(text):
    return text.split()