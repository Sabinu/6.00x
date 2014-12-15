__author__ = 'Sabinu'

import random


def oneTrial():
    """
    Simulates one trial of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns True if all three balls are the same color,
    False otherwise.
    """
    balls = ['r', 'r', 'r', 'g', 'g', 'g']
    chosenBalls = []
    for t in range(3):
        ball = random.choice(balls)
        balls.remove(ball)
        chosenBalls.append(ball)
    if chosenBalls[0] == chosenBalls[1] and chosenBalls[1] == chosenBalls[2]:
        return True
    return False


def noReplacementSimulation_sol(numTrials):
    """
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    """
    numTrue = 0
    for trial in range(numTrials):
        if oneTrial():
            numTrue += 1

    return float(numTrue) / float(numTrials)


def noReplacementSimulation(numTrials):
    """
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    """
    def pick_3():
        lst = [1, 1, 1, 0, 0, 0]
        res = []
        for i in range(3):
            c = random.choice(lst)
            res.append(c)
            lst.remove(c)
        return res

    yes = 0
    for t in range(numTrials):
        test = pick_3()
        if test[0] == test[1] == test[2]:
            yes += 1

    return float(yes) / numTrials


draws = []
for i in range(100):
    draws.append(noReplacementSimulation(100))

print 'Should be:', 1 / 8.0
print 'Could  be:', sum(draws) / len(draws)

draws = []
for i in range(100):
    draws.append(noReplacementSimulation_sol(100))

print 'Should be:', 1 / 8.0
print 'Could  be:', sum(draws) / len(draws)