class Dictionary:
    def __init__(self):
        self.dict = {}
        pass

    def addWord(self, alien_word, italian_words):
        alien_word = alien_word.lower()
        if alien_word in self.dict:
            for word in italian_words:
                if word not in self.dict[alien_word]:
                    self.dict[alien_word].add(word.lower())
        else:
            self.dict[alien_word] = set(word.lower() for word in italian_words)
        pass

    def translate(self, alien_word):
        alien_word = alien_word.lower()
        if alien_word in self.dict:
            return list(self.dict[alien_word])
        return None

    def translateWordWildCard(self, pattern):
        pattern = pattern.lower()
        results = set()
        for alien_word in self.dict.keys():
            if self.isWildcardMatch(pattern, alien_word):
                # Aggiungiamo tutte le traduzioni associate alla parola che matcha [cite: 76]
                results.update(self.dict[alien_word])
        return list(results) if results else None

    def isWildcardMatch(self, pattern, word):
        if len(pattern) != len(word):
            return False
        for i in range(len(pattern)):
            if pattern[i] != '?' and pattern[i] != word[i]:
                return False
        return True