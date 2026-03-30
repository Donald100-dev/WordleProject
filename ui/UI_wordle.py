from game_config.ui_style import *
from gameplay.feedback import WordAndColor
from lib.command_manager import *
from lib.setting_manager import *
from ui.scr_loading import *
from dictionary import *
import time

def treeLine():
    while True:
        print("\r", " "*30, end="", flush=True)
        treeSign_sytle.startStyle()
        print("\r└──>>- ", end="")
        treeText_sytle.startStyle()
        text = input()
        if not text:
            return None
        print(end=">>")
        reset()
        result = command(text)
        match result:
            case True:
                successSign()
            case False:
                failureSign()
            case None:
                meaninglessSign()
        input()

def successSign():
    reset()
    print(" (", end="")
    successSign_sytle.applyStyle(lambda: print("✔ ", end=""))
    print(")", end="")

def failureSign():
    reset()
    print(" (", end="")
    failureSign_sytle.applyStyle(lambda: print("✘ ", end=""))
    print(")", end="")

def meaninglessSign():
    reset()
    print(" (", end="")
    meaninglessSign_sytle.applyStyle(lambda: print("?", end=""))
    print(")", end="")
    
class GameScreen:
    def __init__(self, key_word):
        self.name_game = "WORDLE"
        self.key_word = key_word

    def indent(self, num):
        return (3 - len(str(num))) * " "

    def drawTitleGame(self):
        WIDTH_BOX = 18
        STR_WIDTH = "─" * 18
        Bold_style.startStyle()
        print(f"   ├{STR_WIDTH}┤")
        print("   │", end="    ")
        for i in range(6):
            list_style[i].startStyle()
            print(self.name_game[i], end="")
        reset()
        print("", end=" ")
        text_black.startStyle()
        print("GAME", end="")
        Bold_style.startStyle()
        print("   │")
        print(f"   └{STR_WIDTH}┘")
        reset()

    def printCharColor(self, char, tpyeOfChar):
        if tpyeOfChar is True:
            trueChar_style.startStyle()
            print(char, end="")
        elif tpyeOfChar is False:
            falseChar_style.startStyle()
            print(char, end="")
        else:
            charNotExist_style.startStyle()
            print(char, end="")
        reset()
    
    def printNumberLine(self, num):
        lineNum_style.startStyle()
        print(self.indent(num) + f"{num}| ", end="")
        reset()

    def displayGamePlay(self, past_words, turn) -> None:
        clear_screen()
        self.drawTitleGame()
        for turn in range(len(past_words)):
            self.printNumberLine(turn + 1)
            format_of_word = WordAndColor(past_words[turn], self.key_word)
            Chars_and_color = format_of_word.formatWord()
            for i in range(5):
                self.printCharColor(past_words[turn][i], Chars_and_color[i])
            print() # xuống dòng
            
    def printRejectWord(self, word):
        error_style.startStyle()
        indent_X = 2 * " "
        print(indent_X + "X| ", end="")
        wrongWord_style.startStyle()
        print(word)
        reset()

    def printErrorLenghtWord(self, error_ln) -> None: #3 / 0 / 7; short/equal/long
        if not error_ln: return None
        error_style.startStyle()
        if error_ln == 7: 
            print("   " + get_trans_text()["word"]["too long"])
        else:
            print("   " + get_trans_text()["word"]["too short"])
        reset()
        treeLine()

    def printErrorNotExist(self):
        error_style.startStyle()
        print("   " + get_trans_text()["word"]["not accepted"])
        reset()
        treeLine()

    def StopGame(self):
        input()
        
class EndGame:
    def __init__(self, key_word):
        self.your_chose = None  
        self.key_word = key_word

    def WinOrLose(self, win):
        Bold_style.startStyle()
        if win:
            print("   ]YOU WIN[")
        else:
            print("   ]YOU lOSE[")
        reset()
    
    def showAnswer(self):
        Bold_style.startStyle()
        print(" > ", end=get_trans_text()["message"]["show answer"])
        reset()
        trueChar_style.startStyle()
        print(f"\"{self.key_word}\"")
        reset()
    
    def displayEndGame(self):
        if self.your_chose.strip(" ")[0].lower() != "y":
            Bold_style.startStyle()
            print("OK ✅")
            treeLine()
            reset()
            return None
        clear_screen()
        trueChar_style.startStyle()
        print("> ", self.key_word, end=" ≈ ")
        reset()
        print_translated(self.key_word)
        wait_load_definition = ShowChar()
        wait_load_definition.start()
        data = lookupDefinitionOfword(self.key_word)
        wait_load_definition.stop()
        time.sleep(0.5)
        printDefinitionOfWord(data)
        treeLine()
        
    def viewDefinitions(self):
        Bold_style.startStyle()
        print(" > " + get_trans_text()["message"]["do you want def"])
        reset()
        print("(", end="")
        trueChar_style.startStyle()
        print("Y", end="")
        reset()
        print("/", end="")
        error_style.startStyle()
        print("N", end="")
        reset()
        print(")", end="")
        lighting_style.startStyle()
        print("? :", end="")
        self.your_chose = (input()+"/").strip(" ")[0].upper()
    
