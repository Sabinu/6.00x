__author__ = 'Sabinu'

'''
stuff = (['iBoy', 'iGirl', 'iQ', 'iC', 'iPaid', 'iPad'], )
print type(stuff)
for thing in stuff:
    print thing
    if thing == 'iPad':
        print 'Found it'
'''


def Square(x):
    return SquareHelper(abs(x), abs(x))


def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

print(Square(2))
print(Square(3))
print(Square(0))
print(Square(-2))