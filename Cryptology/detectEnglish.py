#Detect English module
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)
# Edited By Sean Taylor Thomas
UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'
AVG_WORD_LEN = 4

def loadDictionary():
    dictionaryFile = open('dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()

def getEnglishCount(message):
    """ Count number of valid words exist in the message, return a proportion of total words """
    message = message.upper()
    message = removeNonLetters(message)

    matches = 0
    for index in range(len(message) -7):
        word_check = ""
        for i in range(6):
            word_check += message[index+i]
            if word_check in ENGLISH_WORDS:
                matches +=1

    return float(matches) / (len(message)/AVG_WORD_LEN)


def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


def isEnglish(message, wordPercentage=20):
    # By default, 20% of the words must exist in the dictionary file, and
    # 85% of all the characters in the message must be letters or spaces
    # (not punctuation or numbers).
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    return wordsMatch