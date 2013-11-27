import string
PATH_TO_FILE = 'words.txt'


def loadWords():
    inFile = open(PATH_TO_FILE, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print "\t", len(wordlist), "words loaded."
    return wordlist

loadWords()


def loadWords2():
    try:
        inFile = open(PATH_TO_FILE, 'r', 0)
    except IOError:
        print "The wordlist doesn't exist;\nusing some fruits for now."
        return ['apple', 'orange', 'pear', 'lime', 'lemon', 'grape', 'pineapple']
    else:
        line = inFile.readline()
        wordlist = line.split(',')
        print "\t", len(wordlist), "words loaded."
        return wordlist

PATH_TO_FILE = 'words2.txt'
loadWords2()
PATH_TO_FILE = 'doesntExist.txt'
loadWords2()