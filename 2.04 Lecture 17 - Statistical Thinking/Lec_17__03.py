import random
import pylab

#set line width
pylab.rcParams['lines.linewidth'] = 6
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.major.size'] = 5
#set size of numbers on y-axis
pylab.rcParams['ytick.major.size'] = 5


def stdDev(data):
    """ Standard Deviation """
    mean = sum(data) / float(len(data))
    total = 0.0
    for d in data:
        total += (d - mean) ** 2
    return (total / len(data)) ** 0.5


def CV(X):
    """ Coefficient of Variation """
    mean = sum(X) / float(len(X))
    try:
        return stdDev(X) / mean
    except ZeroDivisionError:
        return float('NaN')

##  Problem 4
print(CV([10, 4, 12, 15, 20, 5]))

# # Illustration of Histogram
# vals = []
# for i in range(100000):
#     num = random.random()
#     vals.append(num)
# pylab.hist(vals, bins = 11)
# xmin, xmax = pylab.xlim()
# ymin, ymax = pylab.ylim()
# print 'x-range =', xmin, '-', xmax
# print 'y-range =', ymin, '-', ymax
# pylab.figure
# pylab.hist(vals, bins = 11)
# pylab.xlim(-0.5, 2.0)
# pylab.show()
# assert False


def flip(numFlips):
    heads = 0.0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1.0
    return heads / numFlips


def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads) / len(fracHeads)
    sd = stdDev(fracHeads)
    return fracHeads, mean, sd


def labelPlot(numFlips, numTrials, mean, sd):
    pylab.title(str(numTrials) + ' trials of '
                + str(numFlips) + ' flips each')
    pylab.xlabel('Fraction of Heads')
    pylab.ylabel('Number of Trials')
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    pylab.text(xmin + (xmax - xmin) * 0.02, (ymax - ymin) / 2,
               'Mean = ' + str(round(mean, 4))
               + '\nSD = ' + str(round(sd, 4)))


def makePlots(numFlips1, numFlips2, numTrials):
    val1, mean1, sd1 = flipSim(numFlips1, numTrials)
    pylab.hist(val1, bins = 21)
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    labelPlot(numFlips1, numTrials, mean1, sd1)

    pylab.figure()
    val2, mean2, sd2 = flipSim(numFlips2, numTrials)
    pylab.hist(val2, bins = 21)
    pylab.xlim(xmin, xmax)
    ymin, ymax = pylab.ylim()
    labelPlot(numFlips2, numTrials, mean2, sd2)


pylab.seed(0)
makePlots(100, 1000, 100000)
pylab.show()