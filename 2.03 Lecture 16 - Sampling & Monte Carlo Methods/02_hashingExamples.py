def strToInt(s):
    number = ''
    for c in s:
        number += str(ord(c))
    index = int(number)
    return index

print('\n>>> String to Integer')
print('Index =', strToInt('a'))
print('Index =', strToInt('John is a cool dude'))


def hashStr(s, tableSize = 101):
    number = ''
    for c in s:
        number += str(ord(c))
    index = int(number) % tableSize
    return index

print('\n>>> Hash String')
print('Index =', hashStr('a'))
print('Index =', hashStr('John is a cool dude'))

print('\n>>> Tests:')
print('Hash for Eric  :', hashStr('Eric',   7))
print('Hash for Chris :', hashStr('Chris',  7))
print('Hash for Sarina:', hashStr('Sarina', 7))
print('Hash for Jill  :', hashStr('Jill',   7))