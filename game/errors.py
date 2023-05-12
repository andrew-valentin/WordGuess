from colorama import Fore, Back, Style

def errorMsgLen(len):
    str = f" Please enter a word with {len} letters "
    print(Fore.BLACK + Back.RED + str.center(60, "*"), end="")
    print(Style.RESET_ALL)

def errorMsgWord(word):
    str = " " + word + " is not a valid word "
    print(Fore.BLACK + Back.RED + str.center(60, "*"), end="")
    print(Style.RESET_ALL)

def errorMsgEnd():
    str = " Please enter a valid response "
    print(Fore.BLACK + Back.RED + str.center(60, "*"), end="")
    print(Style.RESET_ALL)