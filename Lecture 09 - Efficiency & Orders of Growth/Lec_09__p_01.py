__author__ = 'Sabinu'


def linearSearch(L, x):
    for i, e in enumerate(L):
        if e == x:
            print i,
            return True
    print 'n',
    return False

print linearSearch([14, 15,  6, 27, 13, 16, 25, 11,  7], 15)
print linearSearch([21,  1, 25, 22, 30, 13,  7, 24, 12], 24)
print linearSearch([20, 10,  1,  7,  4, 22, 25, 12, 31], 20)
print linearSearch([ 9,  3, 12, 24,  7,  8, 23, 11, 19],  8)
print linearSearch([ 4, 12, 20, 17,  9, 14,  7, 24,  6],  7)
print linearSearch([13,  9, 22,  3, 10, 17, 11,  2, 12], 26)