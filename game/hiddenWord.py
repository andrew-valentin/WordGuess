hiddenLetter = '*'

def getHiddenWord(len):
    return hiddenLetter * len

def updateHiddenWord(originalWord, hiddenWord, guess):
    str = hiddenWord
    for i in range(len(originalWord)):
        if (originalWord[i] == guess[i].lower()):
            str = str[:i] + guess[i].lower() + str[i + 1:]

    return str