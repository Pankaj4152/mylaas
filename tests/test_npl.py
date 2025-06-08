from text_image_toolkit.nlp import SentimentAnalyzer, NERTagger

def test_sentiment():
    s = SentimentAnalyzer()
    assert s.analyze("good day") == "positive"
    assert s.analyze("bad day") == "negative"

def test_ner():
    n = NERTagger()
    res = n.tag("Alice in Wonderland")
    assert ("Alice", "ENTITY") in res
    assert ("Wonderland", "ENTITY") in res