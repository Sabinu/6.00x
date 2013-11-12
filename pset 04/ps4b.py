from ps4a import *
import time


def is_valid_word(word, hand):
    """
    @param word    : string
    @param hand    : dictionary - string -> int

    @return        : boolean
                     True if word is entirely composed of letters in the hand.
                     False otherwise.

    Does not mutate hand.
    """
    word_dic = getFrequencyDict(word)
    for l in word_dic:
        if word_dic[l] > hand.get(l, 0):
            return False
    if word not in wordList:
        return False
    else:
        return True


def compChooseWord(hand, wordList, n):
    """
    @param hand    : dictionary - string -> int
    @param wordList: list       - of strings
    @param n       : integer    - HAND_SIZE;
                                  i.e., hand size required for additional points

    @return        : string or None

    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.
    """
    max_score = 0
    best_word = None
    for word in wordList:
        if is_valid_word(word, hand):
            score = getWordScore(word, n)
            if score > max_score:
                max_score = score
                best_word = word
    return best_word


def comp_choose_word(hand, wordList, n):
    """
    @param hand    : dictionary - string -> int
    @param wordList: list       - of strings
    @param n       : integer    - HAND_SIZE;
                                  i.e., hand size required for additional points

    @return        : string     - maximum score considering all words in wordList
                     None       - no words can be made
    """
    max_score = 0
    best_word = None
    for word in wordList:
        if is_valid_word(word, hand):
            score = getWordScore(word, n)
            if score > max_score:
                max_score = score
                best_word = word
    return best_word


def compPlayHand(hand, wordList, n):
    """
    @param hand    : dictionary - string -> int
    @param wordList: list       - of lowercase strings
    @param n       : integer    - HAND_SIZE; i.e., hand size required for additional points

    @return        : None

    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
    """
    total_score = 0
    while calculateHandlen(hand) > 0:
        print '\nCurrent Hand:',
        displayHand(hand)

        word = comp_choose_word(hand, wordList, n)
        if word is None:
            break
        else:
            total_score += getWordScore(word, n)
            print '%r earned %s points. Total: %s points' % (word, getWordScore(word, n), total_score)
            hand = updateHand(hand, word)
    print '>>> COMPU Total score: %s points.\n' % total_score


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1
    """
    hand, user_choice, user_input = None, 'n', None
    while user_choice in ('n', 'r'):
        try:
            user_choice = raw_input('Enter n[new hand], r[replay hand] or e[end game]: ').lower()
            if user_choice == 'e':
                print '\nThank you for playing %r!' % 'The 6.00 Word Game'
                break
            elif user_choice == 'r':
                if hand is None:
                    raise LookupError('No hand played. Please play a new hand first!\n')
            elif user_choice == 'n':
                hand = dealHand(HAND_SIZE)
            else:
                raise ValueError('Invalid command.\n')
        except ValueError, msg:
            user_choice = 'r'
            print msg
        except LookupError, msg:
            print msg
        else:
            while user_input not in ('u', 'c') and user_choice is not None:
                user_input = raw_input('\nEnter u[yourself] or c[computer]: ').lower()
                if user_input not in ('u', 'c'):
                    print 'Invalid command.'
            else:
                if user_input == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                else:
                    compPlayHand(hand, wordList, HAND_SIZE)
                user_input = None

# Build data structures used for entire session and play game
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)

## Test for Computer Choose Word
#print compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)           # appels
#print compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)                   # acta
#print compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)  # immanent
#print compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList, 12)          # None

## Test for Computer Play Hand
#compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)           # 110 points
#compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)                   #  24 points
#compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)  # 105 points