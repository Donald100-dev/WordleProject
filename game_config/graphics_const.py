# Constants for text styles
NORMAL = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
DOUBLE_UNDERLINE = "\033[21m"
STRIKETHROUGH = "\033[9m"

# Constants for text colors (Foreground)
# Note: 29 is often default foreground, 37 is light gray/white, 97 is bright white
GRAY_TEXT = "\033[30m"
RED_TEXT = "\033[31m"
GREEN_TEXT = "\033[32m"
YELLOW_TEXT = "\033[33m"
BLUE_TEXT = "\033[34m" 
MAGENTA_TEXT = "\033[35m" 
CYAN_TEXT = "\033[36m" 
WHITE_TEXT = "\033[37m"
BRIGHT_BLACK_TEXT = "\033[90m"
BRIGHT_RED_TEXT = "\033[91m"
BRIGHT_GREEN_TEXT = "\033[92m"
BRIGHT_YELLOW_TEXT = "\033[93m"
BRIGHT_BLUE_TEXT = "\033[94m"
BRIGHT_MAGENTA_TEXT = "\033[95m"
BRIGHT_CYAN_TEXT = "\033[96m"
BRIGHT_WHITE_TEXT = "\033[97m"


# Constants for background colors
# Note: 39 is often default background, 47 is light gray/white, 107 is bright white
GRAY_BG = "\033[40m"
RED_BG = "\033[41m"
GREEN_BG = "\033[42m"
YELLOW_BG = "\033[43m"
BLUE_BG = "\033[44m"
MAGENTA_BG = "\033[45m"
CYAN_BG = "\033[46m"
WHITE_BG = "\033[47m"
BRIGHT_BLACK_BG = "\033[100m"
BRIGHT_RED_BG = "\033[101m"
BRIGHT_GREEN_BG = "\033[102m"
BRIGHT_YELLOW_BG = "\033[103m"
BRIGHT_BLUE_BG = "\033[104m"
BRIGHT_MAGENTA_BG = "\033[105m"
BRIGHT_CYAN_BG = "\033[106m"
BRIGHT_WHITE_BG = "\033[107m"


# Other effects
INVERT = "\033[7m" # Swap foreground and background colors
HIDDEN = "\033[8m" # Hidden (non-displaying) text - often called NONTEXT
RESET = "\033[0m" # Reset all attributes to default