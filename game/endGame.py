import sys

def win():
    str = " You win! "
    print(str.center(60, "~"))
    print()

def lose(word):
    str = " You lose! "
    print(str.center(60, "~"))
    str = " The word was: '" + word + "' "
    print(str.center(60, "~"))
    print()