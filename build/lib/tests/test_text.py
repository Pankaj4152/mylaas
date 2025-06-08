from text_image_toolkit.text import SimpleTokenizer, simple_lemmatizer, remove_punctuation

def test_tokenizer():
    t = SimpleTokenizer()
    assert t.process("A B C") == ["A", "B", "C"]

def test_lemmatizer():
    assert simple_lemmatizer("cats") == "cat"

def test_cleaner():
    assert remove_punctuation("Hi! Who?") == "Hi Who"