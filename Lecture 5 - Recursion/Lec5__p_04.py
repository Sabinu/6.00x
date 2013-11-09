__author__ = 'Sabinu'


def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == b:
        return a
    s = min(a, b)
    while s > 0:
        if a % s == 0 and b % s == 0:
            return s
        else:
            s -= 1

print gcdIter(99, 11)

print gcdIter(11, 11)

print gcdIter(1, 13)