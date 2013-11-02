__author__ = 'Sabinu'


def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    i1 = min(a, b)
    i2 = max(a, b)

    if i1 == 0:
        return a
    else:
        return gcdRecur(i1, i2%i1)

print gcdRecur(99, 11)

print gcdRecur(11, 11)

print gcdRecur(1, 13)