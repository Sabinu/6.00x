__author__ = 'Sabinu'


def recurPower(base, exp):
    """
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    """
    if exp == 0:
        return 1
    else:
        return recurPower(base, exp-1) * base

print recurPower(2, 2)

print recurPower(2, 3)

print recurPower(2, 4)