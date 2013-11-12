# 6.00x Problem Set 4A Template
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>


import random as r
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b':  3, 'c': 3, 'd': 2, 'e': 1,
    'f': 4, 'g':  2, 'h': 4, 'i': 1, 'j': 8,
    'k': 5, 'l':  1, 'm': 3, 'n': 1, 'o': 1,
    'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
    'u': 1, 'v':  4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


# -----------------------------------
WORDLIST_FILENAME = "words.txt"
def loadWords():
    """
    @return: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    @param sequence: string or list
    @return        : dictionary

    keys   = elements of the sequence
    values = integer counts, for the number of times that
             an element is repeated in the sequence.
    """
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq
# -----------------------------------


def getWordScore(word, n):
    """
    @param word: string  - lowercase letters
    @param    n: integer - HAND_SIZE; i.e., hand size required for additional points)

    @return    : integer - int >= 0 >> score for a word.
                 Assumes the word is a valid word.

    Problem #1: Scoring a word
    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points
    if all n letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)
    """
    if len(word) == 0:
        return 0
    score = 0
    for l in word:
        score += SCRABBLE_LETTER_VALUES[l]
    if len(word) == n:
        return score * len(word) + 50
    else:
        return score * len(word)


def displayHand(hand):
    """
    @param hand: dictionary - string -> int

    Problem #2:
    Displays the letters currently in the hand.

    For example: displayHand({'a':1, 'x':2, 'l':3, 'e':1})
                 Should print out something like:
                    a x x l l l e
                 The order of the letters is unimportant.
    """
    for letter in hand:
        for j in range(hand[letter]):
            print letter,
    print


def dealHand(n):
    """
    @param n: integer    - int >= 0
    @return : dictionary - string -> int
              Random hand containing n lowercase letters.
              At least n/3 the letters in the hand should be VOWELS.

    Problem #2:
    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.
    """
    hand = {}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[r.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[r.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand


def updateHand(hand, word):
    """
    @param hand: dictionary - string -> int
    @param word: string
    @return    : dictionary - string -> int

    Problem #2
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand:
    uses up the letters in the given word and returns
    the new hand, without those letters in it.

    Has no side effects: does not modify hand.
    """
    new_hand = {}
    for k, v in hand.items():
        v -= word.count(k)
        if v > 0:
            new_hand[k] = new_hand.get(k, v)
    return new_hand


def isValidWord(word, hand, wordList):
    """
    @param word    : string
    @param hand    : dictionary - string -> int
    @param wordList: list of lowercase strings

    @return        : boolean
                     True if word is in the wordList and is entirely
                     composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
    """
    word_dic = getFrequencyDict(word)
    for l in word_dic:
        if word_dic[l] > hand.get(l, 0):
            return False
    if word not in wordList:
        return False
    else:
        return True


def calculateHandlen(hand):
    """ 
    @param hand: dictionary - string -> int
    @return    : integer
    Returns the length (number of letters) in the current hand.
    """
    total = 0
    for v in hand.values():
        total += v
    return total


def playHand(hand, wordList, n):
    """
    @param hand    : dictionary - string -> int
    @param wordList: list       - of lowercase strings
    @param n       : integer    - HAND_SIZE; i.e., hand size required for additional points
    @return        : None

    Allows the user to play the given hand, as follows:
    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user inputs a "."
    """
    total_score = 0
    while calculateHandlen(hand) > 0:
        print 'Current Hand:',
        displayHand(hand)

        word = raw_input('Enter word, or a %r to indicate that you are finished: ' % '.')
        if word == '.':
            break
        else:
            if not isValidWord(word, hand, wordList):
                print 'Invalid word, please try again.\n'
            else:
                total_score += getWordScore(word, n)
                print '%r earned %s points. Total: %s points\n' % (word, getWordScore(word, n), total_score)
                hand = updateHand(hand, word)
        if calculateHandlen(hand) == 0:
            print 'Ran out of letters. Total score: %s points.\n' % total_score
            return
    print 'Goodbye! Total score: %s points.\n' % total_score

# Problem #5: Playing a game


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    pass
    # TO DO ... <-- Remove this comment when you code this function
    print "playGame not yet implemented."  # <-- Remove this line when you code the function


# Build data structures used for entire session and play game

if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)

# Case 01
playHand({'h': 1, 'i': 1, 'c': 1,
          'z': 1, 'm': 2, 'a': 1}, wordList, 7)  # him, cam
# Case 02
playHand({'w': 1, 's': 1, 't': 2,
          'a': 1, 'o': 1, 'f': 1}, wordList, 7)  # tow, tasf, fast
# Case 03
playHand({'n': 1, 'e': 1, 't': 1,
          'a': 1, 'r': 1, 'i': 2}, wordList, 7)  # inertia
# Test with variable n; n >= lenHand
