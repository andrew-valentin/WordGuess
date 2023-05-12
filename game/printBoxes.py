from colorama import Fore, Back, Style

hiddenLetter = '*'

def checkLetter(word, hiddenWord, letter):
    for i in range(len(word)):
        if word[i] == letter and hiddenWord[i] == hiddenLetter:
            return True

def printMiddle(word, hiddenWord, guess):
    for i in range(len(word)):
        print(Fore.BLACK + Back.WHITE + "|", end="")
        if word[i] == guess[i]:
            print(Fore.BLACK + Back.GREEN + guess[i], end="")
            print(Style.RESET_ALL, end="")
        elif checkLetter(word, hiddenWord, guess[i]):
            print(Fore.BLACK + Back.YELLOW + guess[i], end="")
            print(Style.RESET_ALL, end="")
        else:
            print(Fore.BLACK + Back.WHITE + guess[i], end="")
            print(Style.RESET_ALL, end="")

    print(Fore.BLACK + Back.WHITE + "|", end="")
    print(Style.RESET_ALL)

def printLine(numLines):
    line = "-"
    print(Fore.BLACK + Back.WHITE + line*(numLines * 2) + "-", end="")
    print(Style.RESET_ALL)

def printBoxes(word, hiddenWord, guess):
    printLine(len(word))
    printMiddle(word, hiddenWord, guess)
    printLine(len(word))