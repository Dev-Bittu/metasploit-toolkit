# Color funcrionts

def black(string: str) -> str:
    return f'\033[30m{str(string)}\033[0m'

def blue(string: str) -> str:
    return f'\033[94m{str(string)}\033[0m'

def gray(string: str) -> str:
    return f'\033[1;30m{str(string)}\033[0m'

def green(string):
    return f'\033[92m{str(string)}\033[0m'

def cyan(string):
    return f'\033[96m{str(string)}\033[0m'

def lightPurple(string):
    return f'\033[94m{str(string)}\033[0m'

def purple(string):
    return f'\033[95m{str(string)}\033[0m'

def red(string):
    return f'\033[91m{str(string)}\033[0m'

def underline(string):
    return f'\033[4m{str(string)}\033[0m'

def white(string):
    return f'\033[0m{str(string)}\033[0m'

def white_2(string):
    return f'\033[1m{str(string)}\033[0m'

def yellow(string):
    return f'\033[93m{str(string)}\033[0m'
