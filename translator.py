from matplotlib import text

from dictionary import Dictionary

class Translator:

    def __init__(self):
        self.dictionary = Dictionary()
        pass

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print("-----------------------\ntranslator Alien-Italian\n-----------------------\n1. Aggiugni nuova parola\n2. Cerca una traduzione\n3. Cerca con wildcard\n4. Exit\n-----------------------")
        pass

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        with open(dict, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if not line or "[" in line: # Salta righe vuote o meta-dati
                        continue
                    parts = line.split()
                    if len(parts) >= 2:
                        alien = parts[0]
                        italians = parts[1:]
                        self.dictionary.addWord(alien, italians)
        pass

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        parts = entry.strip().split()
        if len(parts) < 2:
            return False
        
        alien = parts[0]
        italians = parts[1:]
        
        # Controllo caratteri ammessi 
        if not alien.isalpha():
            return False
            
        self.dictionary.addWord(alien, italians)
        return True        
    pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        if not query.isalpha(): return None
        return self.dictionary.translate(query)

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        if query.count('?') != 1: return None
        return self.dictionary.translateWordWildCard(query)