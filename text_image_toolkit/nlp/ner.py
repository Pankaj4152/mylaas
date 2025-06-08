class NERTagger:
    def tag(self, text):
        # Dummy: tags words starting with capital as 'ENTITY'
        return [(word, "ENTITY") for word in text.split() if word.istitle()]