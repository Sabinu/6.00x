# 6.00 Problem Set 3
# Hangman game


import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."

    inFile = open(WORDLIST_FILENAME, 'r', 0)

    line = inFile.readline()

    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    """
    for l in secretWord:
        if l not in lettersGuessed:
            return False
    else:
        return True


def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    gWord = ''
    for l in secretWord:
        if l in lettersGuessed:
            gWord += l + ' '
        else:
            gWord += '_ '
    return gWord


def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    aLetters = ''
    for l in 'aeiou':
        if l not in lettersGuessed:
            aLetters += l + ' '
    for l in string.ascii_lowercase:
        if l not in lettersGuessed and l not in 'aeiou':
            aLetters += l + ' '
    return aLetters
    

def hangman(secretWord):
    """
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    """
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is %s letters long.' % (len(secretWord))
    print '_____________'
    while True:
        print 'Please select difficulty: easy(e), medium(m), hard(h)'
        print 'Easy   = 10 guesses'
        print 'Medium =  8 guesses'
        print 'Hard   =  6 guesses'
        selection = raw_input('Difficulty: ').lower()
        if selection in 'emh':
            if selection == 'e':
                guesses = 10
            elif selection == 'm':
                guesses = 8
            else:
                guesses = 6
            break
        else:
            print 'Please choose from the listed options; E, M or H.'

    print '_____________'
    lettersGuessed = []
    while guesses > 0:
        print 'You have %s guesses left.' % (guesses)
        print 'Available letters: ' + getAvailableLetters(lettersGuessed)
        gLetter = raw_input('Please guess a letter: ').lower()
        if gLetter and len(gLetter) == 1:
            if gLetter not in lettersGuessed and gLetter in secretWord:
                lettersGuessed.append(gLetter)
                print 'Good guess: ' + getGuessedWord(secretWord, lettersGuessed)
            elif gLetter in lettersGuessed:
                print 'Oops! You\'ve already guessed that letter: ' + getGuessedWord(secretWord, lettersGuessed)
            else:
                lettersGuessed.append(gLetter)
                guesses -= 1
                print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)
        elif not gLetter:
            print 'Please enter a letter this time.'
        else:
            print 'Enter just one letter, please.'
        if isWordGuessed(secretWord, lettersGuessed):
            print '_____________'
            print 'Congratulations, you won!'
            break
        print '_____________'
    else:
        print 'Sorry, you ran out of guesses. The word was %s' % (secretWord.upper())

## HANGMAN PART 1: Is the word guessed?
#secretWord = 'apple'
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print isWordGuessed(secretWord, lettersGuessed)

## HANGMAN PART 1: Printing out the user's guess.
#secretWord = 'apple'
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print getGuessedWord(secretWord, lettersGuessed)

## HANGMAN PART 1: Printing out all available letters.
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print getAvailableLetters(lettersGuessed)

## HANGMAN PART 2: THE GAME
#secretWord = 'tact'
#secretWord = 'else'

while True:
    print '_______________________________________'
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
    print 'Would you like to play again: yes(y) or no(n)'
    selection = raw_input('Select: ').lower()
    if selection == 'n':
        break