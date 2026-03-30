from random import choice
from game_config.ui_style import *
from gameplay.guess_manager import *
from gameplay.word_manager import *
from gameplay.feedback import *
from lib.setting_manager import get_setting_game 
from ui.UI_wordle import *
from lib.utils import *
from dictionary import *
import os , sys

def main():
    LOOPGAME = True
    try:
        first_setting()
        renameConsole(get_setting_game("name game"))
        while LOOPGAME:
            NewGame = WordleGame()
            key_word = randomWordAnswers()
            ScreenGame = GameScreen(key_word)
            is_winer = False
            for turn in range(1, NewGame.guess_turn + 1):
                while True:
                    ScreenGame.displayGamePlay(NewGame.list_past_word, turn)
                    ScreenGame.printNumberLine(turn)
                    word_player_guess = input().strip().lower()
                    error_length = NewGame.checkLenghtWord(word_player_guess)
                    if error_length:
                        ScreenGame.displayGamePlay(NewGame.list_past_word, turn)
                        ScreenGame.printRejectWord(word_player_guess)
                        ScreenGame.printErrorLenghtWord(error_length)
                        continue
                    if NewGame.addWordVail(word_player_guess): break
                    ScreenGame.displayGamePlay(NewGame.list_past_word, turn)
                    ScreenGame.printRejectWord(word_player_guess)
                    ScreenGame.printErrorNotExist()
                ScreenGame.displayGamePlay(NewGame.list_past_word, turn)
                is_answer = all(WordAndColor(word_player_guess, key_word).formatWord())
                if is_answer:
                    is_winer = True
                    break
            end_game = EndGame(key_word)
            end_game.WinOrLose(is_winer)
            end_game.showAnswer()
            end_game.viewDefinitions()
            end_game.displayEndGame()
    except KeyboardInterrupt:
        clear_screen()
        reset()
        sys.exit(0)
    except Exception as e:
        print(e)
        input()
        sys.exit(1)

if __name__ == "__main__":
    main()