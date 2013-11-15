# 6.00x  - Problem Set 5
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"


# -----------------------------------
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList


def isWord(wordList, word):
    """
    Wrapper Function Determines if word is a valid word.

    @param wordList: list    - of strings(words) in the dictionary.
    @param word    : string  - a possible word.

    @return        : boolean - True if word is in wordList.
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList


def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)


def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])


def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()
# -----------------------------------


#
# Problem 1: Encryption
def buildCoder(shift):
    """
    Builds cipher defined by the shift value.

    Ignores non-letter characters like punctuation, numbers and spaces.
    @param shift: integer    - 0 <= __ < 26
    @return     : dictionary - for Caesar cipher
    """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    dict = {}
    for i, l in enumerate(upper):
        dict[l] = upper[(i+shift) % 26]
    for i, l in enumerate(lower):
        dict[l] = lower[(i+shift) % 26]
    return dict


def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    mapp = ''
    for l in text:
        if l in coder.keys():
            mapp += coder[l]
        else:
            mapp += l
    return mapp


def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    return "Not yet implemented."  # Remove this comment when you code the function

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    return "Not yet implemented."  # Remove this comment when you code the function

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    ### TODO.
    return "Not yet implemented."  # Remove this comment when you code the function


# Build data structures used for entire session and run encryption
#if __name__ == '__main__':
#    # To test findBestShift:
#    wordList = loadWords()
#    s = applyShift('Hello, world!', 8)
#    bestShift = findBestShift(wordList, s)
#    assert applyShift(s, bestShift) == 'Hello, world!'
#    # To test decryptStory, comment the above four lines and uncomment this line:
#    #    decryptStory()
