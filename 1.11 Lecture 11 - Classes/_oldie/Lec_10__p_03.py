__author__ = 'Sabinu'


def isPrime(n):
    if type(n) is not int:
        raise TypeError
    if n <= 0:
        raise ValueError
    div = n//2
    while div > 1:
        if n % div == 0:
            return False
        else:
            div -= 1
    return True