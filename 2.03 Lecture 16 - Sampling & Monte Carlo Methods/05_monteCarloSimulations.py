import random


def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1, 2, 3, 4, 5, 6])


def rollLoadedDie():
    if random.random() < 1.0 / 5.5:
        return 6
    else:
        return random.choice([1, 2, 3, 4, 5])


def checkPascal(numTrials, roll):
    yes = 0.0
    for i in range(numTrials):
        for j in range(24):
            d1 = roll()
            d2 = roll()
            if d1 == 6 and d2 == 6:
                yes += 1
                break
    print 'Probability of losing =', 1.0 - yes / numTrials

checkPascal(10000, rollDie)
checkPascal(10000, rollLoadedDie)


def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1
    return heads / float(numFlips)

flips = []
for i in range(100):
    flips.append(flip(10000))

print sum(flips) / len(flips)