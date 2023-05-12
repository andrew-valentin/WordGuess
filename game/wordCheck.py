import json
import requests

def getWord(word):
    return requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word).json()

def checkWord(word):
    if type(word) is list:
        return True
    return False

def validWord(word):
    request = getWord(word)

    return checkWord(request)