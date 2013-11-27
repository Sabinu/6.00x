__author__ = 'Sabinu'


def program1(L):
    multiples = []                      # 1
    for x in L:                         # 1 * n
        for y in L:                     # * 1 * n
            multiples.append(x*y)       # * (3n + 1)
    return multiples                    # 1
# Best  Case = 2                        <<< List is Empty
# Worst Case = 2 + 3 * n^2 + n          <<< List is Full
# Asymptotic Complexity = O(n^2)


def program2(L):
    squares = []                        # 1
    for x in L:                         # 1 * n
        for y in L:                     # * (4 * n + 1)
            if x == y:                  # 1
                squares.append(x*y)     # 3
    return squares                      # 1
# Best  Case = 2                        <<< List is Empty
# Worst Case = 2 + 4 * n^2 + n          <<< List is Full
# Asymptotic Complexity = O(n^2)


def program3(L1, L2):
    intersection = []                   # 1
    for elt in L1:                      # 1 * n
        if elt in L2:                   # * (n + 2)
            intersection.append(elt)    # 1
    return intersection                 # 1
# Best  Case = 2                        <<< Both Lists is Empty
# Worst Case = 2 + 2 * n + n^2          <<< Both Lists are Full & length n
# Asymptotic Complexity = O(n^2)