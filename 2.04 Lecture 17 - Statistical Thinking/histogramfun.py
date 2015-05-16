import pylab


WORDLIST_FILENAME = "words.txt"


def loadWords():
    """ Returns a list of valid words. Words are strings of lowercase letters.
        Depending on the size of the word list, this function may
        take a while to finish. """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("\t", len(wordList), "words loaded.")
    return wordList


def plotVowelProportionHistogram(wordList, numBins=15):
    """ Plots a histogram of the proportion of vowels in each word in wordList
        using the specified number of bins in numBins """
    def count_vowels(word):
        v = 0
        for l in word:
            if l.lower() in 'aeiou':
                v += 1
        return v

    prop = []
    for w in wordList:
        prop.append(count_vowels(w) / float(len(w)))

    pylab.title('Histogram of Vowel Proportion in set of Words')
    pylab.xlabel('Proportion of Vowels')
    pylab.ylabel('Number of Words')

    pylab.hist(prop, numBins)
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    pylab.text(xmin + (xmax - xmin) * 0.02, ymax * 0.93,
               'Total Number of Words = ' + str(len(prop)))

    pylab.show()

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)