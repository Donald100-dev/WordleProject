from game_config.ui_style import *

class WordAndColor:
    def __init__(self, word, key_word):
        self.chars = list(word)
        self.key_chars = list(key_word)
        self.LENGHT_OF_WORD = 5
        self._CHAR_ERROR = "_"
    
    def formatWord(self):
        for i in range(self.LENGHT_OF_WORD):
            if self.chars[i] == self.key_chars[i]:
                self.key_chars[i] = self._CHAR_ERROR
                self.chars[i] = True
        for i in range(self.LENGHT_OF_WORD):
            if not isinstance(self.chars[i], str): continue
            if self.chars[i] not in self.key_chars:
                self.chars[i] = None
                continue
            index_char = self.key_chars.index(self.chars[i])
            self.key_chars[index_char] = self._CHAR_ERROR
            self.chars[i] = False
        return self.chars
