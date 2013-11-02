def square(x):
    '''
    x: int or float.
    '''
    return x * x

def fourthPower(x):
    '''
    x: int or float.
    '''
    return square(square(x))

def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    ans = x%2
    return bool(ans)
    
def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    vocale = 'aeiouAEIOU'
    i = 0
    while i < len(vocale):
        if char == vocale[i]:
            return True
        else: i += 1
    return False

def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    vocale = 'aeiouAEIOU'
    for i in vocale:
        if char == i:
            return True
    return False
    
print ('a = ' + str(isVowel2('a')))
print ('U = ' + str(isVowel2('U')))
print ('t = ' + str(isVowel2('t')))