__author__ = 'Sabinu'

import pylab

PATH_TO_FILE = 'julyTemps.txt'


def load_words():
    try:
        inFile = open(PATH_TO_FILE, 'r')
    except IOError:
        print("No file for July Temperature.")
    high = []
    low = []
    line = inFile.readline()
    while line:
        fields = line.split(' ')
        if len(fields) == 3 and fields[0].isdigit():
            high.append(int(fields[1]))
            low.append(int(fields[2]))
        line = inFile.readline()
    inFile.close()

    print('>>>', len(high), "temperatures loaded.")
    loaded = (high, low)
    return loaded


def producePlot(lowTemps, highTemps):
    diffTemps = []
    for i in range(len(lowTemps)):
        diffTemps.append(highTemps[i] - lowTemps[i])

    pylab.plot(range(1, len(lowTemps)+1), diffTemps, 'r', linewidth=2)

    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012', fontsize=12)
    pylab.xlabel('Days', fontsize=10)
    pylab.ylabel('Temperature Ranges', fontsize=10)
    pylab.show()

jt = load_words()
producePlot(jt[1], jt[0])