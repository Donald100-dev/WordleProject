from game_config.creat_style import *
from game_config.graphics_const import *

#error
error_style = color()
error_style.setColor(text=RED_TEXT)
error_style.setfonts(BOLD)

#word
charNotExist_style = color()
charNotExist_style.setColor(text=GRAY_TEXT)
charNotExist_style.setfonts(BOLD, UNDERLINE)

falseChar_style = color()
falseChar_style.setColor(text=YELLOW_TEXT)
falseChar_style.setfonts(BOLD, UNDERLINE)

trueChar_style = color()
trueChar_style.setColor(text=GREEN_TEXT)
trueChar_style.setfonts(BOLD, UNDERLINE)

wrongWord_style = color()
wrongWord_style.setColor(text=RED_TEXT)
wrongWord_style.setfonts(ITALIC, STRIKETHROUGH)

lineNum_style = color()
lineNum_style.setColor(text=CYAN_TEXT)
lineNum_style.setfonts(BOLD)

Bold_style = color()
Bold_style.setColor(text=WHITE_TEXT)
Bold_style.setfonts(BOLD)

NoConnection_style = color()
NoConnection_style.setColor(text=CYAN_TEXT)
NoConnection_style.setfonts(BOLD, DIM)

Dim_style = color()
Dim_style.setColor(text=BLUE_TEXT)
Dim_style.setfonts(DIM)

lighting_style = color()
lighting_style.setColor(text=YELLOW_TEXT)
lighting_style.setfonts(BOLD)

title_style = color()
title_style.setColor(text=CYAN_TEXT)
title_style.setfonts(BOLD)

#tree line
treeSign_sytle = color()
treeSign_sytle.setColor(text=BLUE_TEXT)
treeSign_sytle.setfonts(BOLD, DIM)

successSign_sytle = color()
successSign_sytle.setColor(text=GREEN_TEXT)
successSign_sytle.setfonts(BOLD)

failureSign_sytle = color()
failureSign_sytle.setColor(text=RED_TEXT)
failureSign_sytle.setfonts(BOLD)

meaninglessSign_sytle = color()
meaninglessSign_sytle.setColor(text=MAGENTA_TEXT)
meaninglessSign_sytle.setfonts(ITALIC, BOLD)

treeText_sytle = color()
treeText_sytle.setColor(text=BLUE_TEXT)
treeText_sytle.setfonts(BOLD, DIM, ITALIC)

#loading
hidden_style = color()
hidden_style.setColor(text=GRAY_TEXT)
hidden_style.setfonts(DIM, BOLD)

#title game
list_color = [
            BRIGHT_RED_TEXT, BRIGHT_CYAN_TEXT,
            BRIGHT_GREEN_TEXT, BRIGHT_MAGENTA_TEXT,
            BRIGHT_YELLOW_TEXT, BRIGHT_CYAN_TEXT
            ]
list_style = []
for COLOR_STYLE in list_color:
    style = color()
    style.setColor(text=COLOR_STYLE)
    style.setfonts(BOLD)
    list_style.append(style)

text_black = color()
text_black.setColor(text=WHITE_TEXT)
text_black.setfonts(BOLD)