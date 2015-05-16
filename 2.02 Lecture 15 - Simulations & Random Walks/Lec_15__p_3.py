__author__ = 'Sabinu'

import random


def deterministicNumber():
    """
    Deterministically generates an even number.
    Between 9 and 21.
    """
    # return 10 # or 12 or 14 or 16 or 18 or 20

    random.seed(0)
    return 2 * random.randint(5, 10)

def stocasticNumber():
    """
    Stochastically generates a uniformly distributed even number.
    Between 9 and 21.
    """
    return random.choice(range(10, 21, 2))

for i in range(10):
    print deterministicNumber().next(), stocasticNumber()