from game_config.graphics_const import *
import sys

class color:
    def __init__(self):
        self.Text = ""
        self.Background = ""
        self.Fonts = []

    def setColor(self,  *, text = NORMAL, background = NORMAL):
        self.Text = text
        self.Background = background

    def setfonts(self, *args):
        self.Fonts = args
        
    def applyStyle(self, func):
        self.startStyle()
        result = func()
        reset()
    
    def startStyle(self):
        reset()
        for font in self.Fonts:
            sys.stdout.write(font)
        if self.Text != NORMAL:
            sys.stdout.write(self.Text)
        if self.Background != NORMAL:
            sys.stdout.write(self.Background)

def reset():
    sys.stdout.write(RESET)

