__author__ = 'Sabinu'


def program1(x):
    total = 0                           # 1
    for i in range(1000):               # 1 * 1000
        total += i                      # 2 * 1000

    while x > 0:                        # 1 * n
        x -= 1                          # 2 * n
        total += x                      # 2 * n

    return total                        # 1
# Best  Case = 3003
# Worst Case = 3003 + 5 * n


def program2(x):
    total = 0                           # 1
    for i in range(1000):               # 1 * 1000
        total = i                       # 1 * 1000

    while x > 0:                        # 1 * log2(n)
        x /= 2                          # 2 * log2(n)
        total += x                      # 2 * log2(n)

    return total
# Best  Case = 2003
# Worst Case = 2008 + 5 * log2(n)

def program3(L):
    totalSum = 0                        # 1
    highestFound = None                 # 1
    for x in L:                         # 1 * n
        totalSum += x                   # 2 * n

    for x in L:                         # 1 +          & (n-1)
        if highestFound is None:        # 1 first time & 1 * (n-1) the rest
            highestFound = x            # 1
        elif x > highestFound:          # 1 * (n-1)
            highestFound = x            # 1 * (n-1)

    return (totalSum, highestFound)     # 1
# Best  Case = 3                        <<< List is Empty
# Worst Case = 2 + 7 * n