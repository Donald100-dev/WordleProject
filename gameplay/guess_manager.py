from gameplay.word_manager import *
class WordleGame:
    def __init__(self, guess_turn=6):
        self.list_past_word = []
        self.level = "easy"
        self.guess_turn = guess_turn
    
    def checkLenghtWord(self,word):
        ln = len(word)
        if ln == 5:
            return 0
        elif ln > 5:
            return 7
        else:
            return 3

    def addWordVail(self, word) -> bool:
        if word in words:
            self.list_past_word.append(word)
            return True
        return False
    
    def setLevelhard(level):
        if level == "hard":
            self.level = "hard"


    