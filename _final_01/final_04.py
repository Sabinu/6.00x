__author__ = 'Sabinu'


def is_it(num, secret):
    if num < secret:
        return -1
    elif num == secret:
        return 0
    else:
        return 1


def is_it_min_5(num):
    return is_it(num, -5)


def is_it_pl__1(num):
    return is_it(num, 1)

def is_it_pl_10(num):
    return is_it(num, 10)

def jumpAndBackpedal(isMyNumber):
    """
    isMyNumber: Procedure that hides a secret number.
    It takes as a parameter one number and returns:
       -1 if the number is less than the secret number
        0 if the number is equal to the secret number
        1 if the number is greater than the secret number

    returns: integer, the secret number
    """
    guess = 1
    foundNumber = False
    while not foundNumber:
        if isMyNumber(guess) == 0:
            foundNumber = True
        sign = isMyNumber(guess)
        guess -= sign
    return guess


print jumpAndBackpedal(is_it_min_5)
print jumpAndBackpedal(is_it_pl__1)
print jumpAndBackpedal(is_it_pl_10)