__author__ = 'Sabinu'


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    if len(aStr) == 1:
        if aStr[0] == char:
            return True
        else:
            return False

    if aStr[len(aStr) / 2] == char:
        return True
    elif char < aStr[len(aStr)/2]:
        return isIn(char, aStr[0:len(aStr)/2])
    else:
        return isIn(char, aStr[len(aStr)/2 + 1:len(aStr)])

char = 'f'
aStr = 'abcdefghijklmnopqrs'

print str(isIn(char, aStr)) + ': ' + char + ' is in ' + aStr