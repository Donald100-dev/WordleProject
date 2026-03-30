from lib.setting_manager import *
from lib.utils import get_resource_path
import random, os

base_path = os.path.join(get_resource_path(), "lib", "data")

wordle_words_path = os.path.join(base_path, "wordle-words.txt")
wordle_answers_path = os.path.join(base_path, "wordle-answers.txt")
top500_5letter_path = os.path.join(base_path, "top500_5letter.txt")

with open(wordle_words_path, "r") as file_word:
    words = file_word.read().split("\n")
with open(wordle_answers_path, "r") as file_word:
    answers_random = file_word.read().split("\n")
with open(top500_5letter_path, "r") as file_word:
    answers_easy = file_word.read().split("\n")

def randomWordAnswers():
    level = get_setting_game("level")
    if level == "easy":
        return random.choice(answers_easy)
    elif level == "hard":
        return random.choice(answers_random)
