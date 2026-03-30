import requests, os, sys, shutil

def renameConsole(name_game="my game"):
    if os.name == "nt":
        os.system(f"title {name_game}")
    else:
        os.system(f'echo -ne "\033]0;{title}\a"')
    
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_data_path(file_name):
    appdata_path = os.getenv('APPDATA')
    app_folder_path = os.path.join(appdata_path, 'WordleGame', 'data')
    if not os.path.exists(app_folder_path):
        os.makedirs(app_folder_path)
    return os.path.join(app_folder_path, file_name)

def first_setting():
    base_path = os.path.join(get_resource_path(), "lib", "data")
    app_folder_path = get_data_path("")
    if os.listdir(app_folder_path): return None
    setting_game_path = os.path.join(base_path, "game.json")
    setting_text_path = os.path.join(base_path, "texts.json")
    shutil.copy(setting_game_path, os.path.join(app_folder_path, "game.json"))
    shutil.copy(setting_text_path, os.path.join(app_folder_path, "texts.json"))

def get_resource_path():
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    return base_path

def canConnected():
    try:
        requests.get("https://www.google.com")
        return True
    except requests.ConnectionError:
        return False