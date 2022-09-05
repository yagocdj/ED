# Clear terminal by GeeksForGeeks
from os import system, name


def clearTerminal() -> None:

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
