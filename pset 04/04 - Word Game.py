# 6.00x Problem Set 4
#
# The 6.00 Word Game
# Created  by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sabin Purice


import random as r
import string
import time

WORDLIST_FILENAME = "words.txt"

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b':  3, 'c': 3, 'd': 2, 'e': 1,
    'f': 4, 'g':  2, 'h': 4, 'i': 1, 'j': 8,
    'k': 5, 'l':  1, 'm': 3, 'n': 1, 'o': 1,
    'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
    'u': 1, 'v':  4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}


def load_words():
    """
    @return: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "\t", len(wordList), "words loaded."
    return wordList


def get_freq_dict(sequence):
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


def get_word_score(word, n):
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


def hand_display(hand):
    """
    @param hand: dictionary - string -> int

    Problem #2:
    Displays the letters currently in the hand.

    For example: hand_display({'a':1, 'x':2, 'l':3, 'e':1})
                 Should print out something like:
                    a x x l l l e
                 The order of the letters is unimportant.
    """
    for letter in hand:
        for j in range(hand[letter]):
            print letter,
    print


def hand_deal(n):
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


def hand_update(hand, word):
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


def valid_word(word, hand, w_list):
    """
    @param word    : string
    @param hand    : dictionary - string -> int
    @param w_list: list of lowercase strings

    @return        : boolean
                     True if word is in the word_list and is entirely
                     composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or word_list.
    """
    word_dic = get_freq_dict(word)
    for l in word_dic:
        if word_dic[l] > hand.get(l, 0):
            return False
    if word not in w_list:
        return False
    else:
        return True


def calc_hand_len(hand):
    """ 
    @param hand: dictionary - string -> int
    @return    : integer    - nr. of letters in the current hand.
    """
    total = 0
    for v in hand.values():
        total += v
    return total


def human_play_hand(hand, w_list, n):
    """
    @param hand    : dictionary - string -> int
    @param w_list: list       - of lowercase strings
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
    while calc_hand_len(hand) > 0:
        print '\nCurrent Hand:',
        hand_display(hand)

        word = raw_input('Enter %r[continue] or %r[terminate]: ' % ('word', '.'))
        if word == '.':
            break
        else:
            if not valid_word(word, hand, w_list):
                print 'Invalid word, please try again.'
            else:
                total_score += get_word_score(word, n)
                print '%r earned %s points. Total: %s points' % (word, get_word_score(word, n), total_score)
                hand = hand_update(hand, word)
        if calc_hand_len(hand) == 0:
            print '\nRan out of letters. Total score: %s points.' % total_score
            return
    print '>>> HUMAN Total score: %s points.\n' % total_score


def comp_valid_word(word, hand):
    """
    @param word    : string
    @param hand    : dictionary - string -> int

    @return        : boolean
                     True if word is entirely composed of letters in the hand.
                     False otherwise.

    Does not mutate hand.
    """
    word_dic = get_freq_dict(word)
    for l in word_dic:
        if word_dic[l] > hand.get(l, 0):
            return False
    if word not in word_list:
        return False
    else:
        return True


def comp_choose_word(hand, w_list, n):
    """
    @param hand    : dictionary - string -> int
    @param w_list: list       - of strings
    @param n       : integer    - HAND_SIZE;
                                  i.e., hand size required for additional points

    @return        : string     - maximum score considering all words in word_list
                     None       - no words can be made
    """
    max_score = 0
    best_word = None
    for word in w_list:
        if comp_valid_word(word, hand):
            score = get_word_score(word, n)
            if score > max_score:
                max_score = score
                best_word = word
    return best_word


def comp_play_hand(hand, w_list, n):
    """
    @param hand    : dictionary - string -> int
    @param w_list: list       - of lowercase strings
    @param n       : integer    - HAND_SIZE; i.e., hand size required for additional points

    @return        : None

    Allows the computer to play the given hand, following the same procedure
    as human_play_hand, except instead of the user choosing a word, the computer
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
    while calc_hand_len(hand) > 0:
        print '\nCurrent Hand:',
        hand_display(hand)

        word = comp_choose_word(hand, w_list, n)
        if word is None:
            break
        else:
            total_score += get_word_score(word, n)
            print '%r earned %s points. Total: %s points' % (word, get_word_score(word, n), total_score)
            hand = hand_update(hand, word)
    print '>>> COMPU Total score: %s points.\n' % total_score


def one_play_game(w_list):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1
    """
    hand, user_input = None, 'n'
    while user_input in ('n', 'r'):
        user_input = raw_input('Enter n[new hand], r[replay hand] or e[end game]: ').lower()
        if user_input == 'e':
            print '\nThank you for playing %r!' % 'The 6.00 Word Game'
            break
        elif user_input == 'n':
            hand = hand_deal(HAND_SIZE)
            human_play_hand(hand, w_list, HAND_SIZE)
        elif user_input == 'r':
            if hand is None:
                print 'You have not played a hand yet. Please play a new hand first!\n'
            else:
                human_play_hand(hand, w_list, HAND_SIZE)
        else:
            user_input = 'r'
            print 'Invalid command.\n'


def two_play_game(w_list):
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
          with the selected hand, using human_play_hand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using comp_play_hand.

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
                hand = hand_deal(HAND_SIZE)
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
                    human_play_hand(hand, w_list, HAND_SIZE)
                else:
                    comp_play_hand(hand, w_list, HAND_SIZE)
                user_input = None


# Build data structures used for entire session and play game
if __name__ == '__main__':
    word_list = load_words()
    two_play_game(word_list)
