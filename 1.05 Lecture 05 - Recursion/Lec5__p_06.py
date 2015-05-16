__author__ = 'Sabinu'


def lenIter(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    length = 0
    for c in aStr:
        length += 1
    return length


def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    if aStr == '':
        #print('\n')
        return 0
    #print aStr
    return lenRecur(aStr[1:]) + 1

print lenRecur('abcef 032')