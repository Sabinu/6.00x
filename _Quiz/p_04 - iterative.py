__author__ = 'Sabinu'

def myLog(x, b):
    """
    @param x: a positive integer
    @param b: a positive integer; b >= 2
    @return : log_b(x), or, the logarithm of x relative to a base b.
    """
    r = 1
    t = b
    while t <= x:
        t *= b
        r += 1
    return r - 1


print myLog(15,  3)  # 2
print myLog(16,  2)  # 4
print myLog(15,  3)  # 2
print myLog(234, 2)  # 7