import json
from lib.utils import get_data_path

def get_setting_game(name):
    FILE_GAME = get_data_path("game.json")
    with open(FILE_GAME, "r") as infor_game:
        setup_game = json.load(infor_game)
        infor = setup_game.get(name, f"'{name}'")
    return infor

def get_trans_text():
    try:
        FILE_TEXT = get_data_path("texts.json")
        with open(FILE_TEXT, "r", encoding='utf-8') as file_texts:
            texts = json.load(file_texts)
            return texts
    except:
        return None

def set_setting_game(name, val):
    FILE_GAME = get_data_path("game.json")
    with open(FILE_GAME, "r") as infor_game:
        data = json.load(infor_game)
    data[name] = val
    with open(FILE_GAME, "w") as infor_game:
        json.dump(data, infor_game, indent=4)