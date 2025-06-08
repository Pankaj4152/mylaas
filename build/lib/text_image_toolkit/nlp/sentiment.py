class SentimentAnalyzer:
    def analyze(self, text):
        # Dummy: positive if 'good' in text
        return "positive" if "good" in text else "negative"