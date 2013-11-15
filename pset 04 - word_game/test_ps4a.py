from ps4a import *

# TEST CODE
# =========


def digits(nr):
    """
    @param : integer
    @return: digit length of nr
    """
    dig = 1
    while nr > 10:
        nr //= 10
        dig += 1
    return dig


def test_getWordScore():
    """
    Unit test for getWordScore
    """
    failure = False
    words = {("",        7):   0, ("it",      7):   4, ("was",  7): 18,
             ("scored",  7):  54, ("waybill", 7): 155,
             ("outgnaw", 7): 127, ("fork",    7):  44, ("fork", 4): 94}
    for (word, n) in words.keys():
        score = getWordScore(word, n)
        eScore = words[(word, n)]
        scSpace = ''
        stSpace = ''
        if score != eScore:
            for l in range(3 - digits(eScore)):
                scSpace += ' '
            for l in range(7 - len(word)):
                stSpace += ' '
            print "FAILURE:",
            print "Exp" + scSpace, eScore, \
                "pnts /// got '" + str(score) + "' for '" \
                + word + "'," + stSpace + " n = " + str(n)
            failure = True
        #else:
        #    print "\tSUCCESS: for '" + word +"'"
    if not failure:
        print "SUCCESS: Test Get Word Score"


def test_updateHand():
    """
    Unit test for updateHand
    """
    # test 1
    handOrig = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
    handCopy = handOrig.copy()
    word = "quail"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {'l': 1, 'm': 1}
    expectedHand2 = {'a': 0, 'q': 0, 'l': 1, 'm': 1, 'u': 0, 'i': 0}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print "FAILURE: test_updateHand('" + word + "', " + str(handOrig) + ")"
        print "\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2
        return
    if handCopy != handOrig:
        print "FAILURE: test_updateHand('"+ word + "', " + str(handOrig) + ")"
        print "\tOriginal hand was", handOrig
        print "\tbut implementation of updateHand mutated the original hand!"
        print "\tNow the hand looks like this:", handCopy
        return
        
    # test 2
    handOrig = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}
    handCopy = handOrig.copy()
    word = "evil"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {'v': 1, 'n': 1, 'l': 1}
    expectedHand2 = {'e': 0, 'v': 1, 'n': 1, 'i': 0, 'l': 1}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print "FAILURE: test_updateHand('" + word + "', " + str(handOrig) + ")"
        print "\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2
        return
    if handCopy != handOrig:
        print "FAILURE: test_updateHand('" + word + "', " + str(handOrig) + ")"
        print "\tOriginal hand was", handOrig
        print "\tbut implementation of updateHand mutated the original hand!"
        print "\tNow the hand looks like this:", handCopy
        return

    # test 3
    handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    handCopy = handOrig.copy()
    word = "hello"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {}
    expectedHand2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print "FAILURE: test_updateHand('" + word + "', " + str(handOrig) + ")"
        print "\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2
        return
    if handCopy != handOrig:
        print "FAILURE: test_updateHand('" + word + "', " + str(handOrig) + ")"
        print "\tOriginal hand was", handOrig
        print "\tbut implementation of updateHand mutated the original hand!"
        print "\tNow the hand looks like this:", handCopy
        return

    print "SUCCESS: Test Update Hand"


def test_isValidWord(wordList):
    """
    Unit test for isValidWord
    """
    failure = False

    # test 1
    word = "hello"
    handOrig = getFrequencyDict(word)
    handCopy = handOrig.copy()
    if not isValidWord(word, handCopy, wordList):
        print "FAILURE:",
        print "Exp True, but got False for word: '" + word + "' and hand:", handOrig
        failure = True

    # Test a second time to see if wordList or hand has been modified
    if not isValidWord(word, handCopy, wordList):
        print "FAILURE:",
        if handCopy != handOrig:
            print "Testing word", word, "for a second time - be sure you're not modifying hand."
            print "\tAt this point, hand ought to be", handOrig, "but it is", handCopy
        else:
            print "Testing word", word, "for a second time - have you modified wordList?"
            wordInWL = word in wordList
            print "\t\t The word", word, "should be in wordList - is it?", wordInWL
        print "\t\t Exp True, but got False for word: '" + word + "' and hand:", handCopy
        failure = True

    # test 2
    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}
    word = "rapture"
    if isValidWord(word, hand, wordList):
        print "FAILURE:",
        print "Exp False, but got True for word: '" + word + "' and hand:", hand
        failure = True

    # test 3
    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}
    word = "honey"
    if not isValidWord(word, hand, wordList):
        print "FAILURE:",
        print "Exp True, but got False for word: '" + word + "' and hand:", hand
        failure = True                        

    # test 4
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u': 2}
    word = "honey"
    if isValidWord(word, hand, wordList):
        print "FAILURE:",
        print "Exp False, but got True for word: '" + word + "' and hand:", hand
        failure = True

    # test 5
    hand = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}
    word = "evil"
    if not isValidWord(word, hand, wordList):
        print "FAILURE:",
        print "Exp True, but got False for word: '" + word + "' and hand:", hand
        failure = True

    # test 6
    word = "even"
    if isValidWord(word, hand, wordList):
        print "FAILURE:",
        print "Exp False, but got True for word: '" + word + "' and hand:", hand
        print "\t(If this is the only failure, make sure isValidWord() isn't mutating its inputs)"
        failure = True        

    # test 7
    word = ''
    if isValidWord(word, hand, wordList):
        print "FAILURE:",
        print "Exp False, but got True for word: '" + word + "' and hand:", hand
        failure = True

    if not failure:
        print "SUCCESS: Test Is Valid Word"


print "======================================================================"
wordList = loadWords()
print "======================================================================"
print "Testing getWordScore..."
print "-----------------------"
test_getWordScore()
print "======================================================================"
print "Testing updateHand..."
print "-----------------------"
test_updateHand()
print "======================================================================"
print "Testing isValidWord..."
print "-----------------------"
test_isValidWord(wordList)
print "======================================================================"
print "All done!"
