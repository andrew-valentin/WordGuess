import json
import requests
import sys

from endGame import *
from errors import *
from hiddenWord import *
from printBoxes import *
from wordCheck import validWord

def endQuestion():
    str = "Enter 'exit' to quit or 'continue' to play again"
    print(str.center(60))
    
    while (True):
        str = input()

        if (str.lower() == 'exit'):
            sys.exit()
        elif(str.lower() == 'continue'):
            gameLoop(getWord())
        else:
            errorMsgEnd()

def gameLoop(word):
    guess = 1
    userGuess = ''
    hiddenWord = getHiddenWord(len(word))

    str = f" Word Length: {len(word)} letters "
    print("\n")
    print(str.center(60, "-"))
    print("\n")

    while (True):
        if (userGuess == word):
            win()
            endQuestion()
        elif(guess == 10):
            lose(word)
            endQuestion()

        userGuess = input(f"Guess {guess}: ")

        if len(userGuess) != len(word):
            errorMsgLen(len(word))
            continue
        elif not validWord(userGuess):
            errorMsgWord(userGuess)
            continue

        hiddenWord = updateHiddenWord(word, hiddenWord, userGuess)
        printBoxes(word, hiddenWord, userGuess)

        guess += 1

def playGame(word):
    print("\n")
    str = " Welcome to Word Guess! "
    print(str.center(60, "~"))
    str = " You will have 10 tries to guess a random word! "
    print(str.center(60, "~"))
    str = " Good luck! "
    print(str.center(60, "~"))

    gameLoop(word)

def getWord():
    return requests.get("https://random-word-api.herokuapp.com/word").json()[0]

def wordGuess():
    playGame(getWord())  