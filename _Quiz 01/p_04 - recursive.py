__author__ = 'Sabinu'


def myLog(x, b):
    """
    x       : a positive integer
    b       : a positive integer; b >= 2
    returns : log_b(x), or, the logarithm of x relative to a base b.
    """
    if x < b:
        return 0
    else:
        return 1 + myLog(x/b, b)

print myLog(15,  3)  # 2
print myLog(16,  2)  # 4
print myLog(15,  3)  # 2
print myLog(234, 2)  # 7