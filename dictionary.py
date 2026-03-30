from deep_translator import GoogleTranslator
from game_config.ui_style import *
from game_config.graphics_const import *
from lib.setting_manager import *
from lib.utils import *
from ui.scr_loading import ProcessProgress
import requests, json

Translator = GoogleTranslator(source='en', target='en')

def _errorNotTrans():
    text_error_trans = get_trans_text()["error trans"]
    text1 = lambda: print(text_error_trans, end="")
    NoConnection_style.applyStyle(text1)

def _transText(source_text) -> str:
    source_language = get_setting_game("source language")
    target_language = get_setting_game("target language")
    if source_language == target_language: return source_text
    Translator = GoogleTranslator(source=source_language, target=target_language)
    if not canConnected():
        return source_text
    try: result = Translator.translate(source_text)
    except: 
        _errorNotTrans()
        return source_text
    return result

def language_switch():
    FILE_GAME = get_data_path("game.json")
    FILE_TEXT = get_data_path("texts.json")
    with open(FILE_GAME, "r", encoding="utf-8") as file_texts:
        setting_game = json.load(file_texts)
        trans_texts = transDictText(setting_game["texts"])
    with open(FILE_TEXT, "w") as file_texts:
        json.dump(trans_texts, file_texts,  indent=4)

def autoTransEnglish(language):
    if not canConnected():
        return language
    try: result = GoogleTranslator(src="auto", dest="en").translate(language)
    except: 
        _errorNotTrans()
        return language
    return result

def transDictText(dict_text, bar_progress=None, val_update=(100/8)):
    trans = {}
    if bar_progress is None:
        LENGTH_BAR_PROGRESS_TRANS = 30
        bar_progress = ProcessProgress(LENGTH_BAR_PROGRESS_TRANS)
        
    for name, text in dict_text.items():
        if isinstance(text, dict):
            trans[name] = transDictText(text, bar_progress)
        else:
            trans[name] = _transText(text)
            bar_progress.update_progress(val_update)
            print(bar_progress, end="", flush=True)
    return trans

def print_translated(*args, sep=" ", end="\n"):
    for text in args:
        print(_transText(text), end=sep)
    print(end=end)

def lookupDefinitionOfword(word):
    if not canConnected():
        return None
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return None
        list_data = response.json()
        if not list_data: return None
        data = list_data[0]
        if not data: return None
        processed_data = {
            "word" : data["word"],
            "phonetics" : data.get("phonetic", ""),
            "meanings" : data["meanings"]
        }
    except:
        return None
    return processed_data

def checkErrorData(data):
    if not canConnected():
        NoConnection_style.applyStyle(
            lambda: print(get_trans_text()["no internet"]))
        return 110
    elif data is None:
        error_style.applyStyle(
            lambda: print(get_trans_text()["no found"]))
        return 404
    return 0

def printDefinitionOfWord(data):
    if not canConnected():
        NoConnection_style.startStyle()
        print(get_trans_text()["error trans"])
        reset()
        return None

    if data is None:
        error_style.startStyle()
        print(get_trans_text()["no found"])
        reset()
        return None

    trueChar_style.startStyle()
    print(data['word'], end="")
    Dim_style.startStyle()
    print(" ",data["phonetics"])
    for meaning in data["meanings"]:
        lighting_style.startStyle()
        print_translated("meanings", end=" ")
        reset()
        print_translated(f"({meaning["partOfSpeech"]})")
        text_definition = ""
        for definition in meaning["definitions"]:
            text_definition += "  -  " + definition["definition"] + "\n"
        print(end="  ")
        print_translated(text_definition)