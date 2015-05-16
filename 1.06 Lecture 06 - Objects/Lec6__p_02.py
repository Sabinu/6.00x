__author__ = 'Sabinu'


def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    i = 1
    bTup = ()
    for e in aTup:
        if i%2 == 1:
            bTup += (e, )
        i += 1
    return bTup

print oddTuples(())
print oddTuples((10,))
print oddTuples((14, 15, 1, 4, 8, 15, 20))
print oddTuples((20, 15, 15, 2))
print oddTuples(('I', 'am', 'a', 'test', 'tuple'))