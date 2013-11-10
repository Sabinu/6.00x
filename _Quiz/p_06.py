__author__ = 'Sabinu'


def laceStringsRecur(s1, s2):
    """
    @param s1 : string
    @param s2 : string
    @return   : str with elements of s1 and s2 interlaced,
                beginning with s1. If strings are not of same length,
                then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return out + s2
        if s2 == '':
            return out + s1
        else:
            return helpLaceStrings(s1[1:], s2[1:], out + s1[0] + s2[0])
    return helpLaceStrings(s1, s2, '')

## TEST SUITE
print laceStringsRecur('abcd',   '12345'), '\n____________'
print laceStringsRecur('123456', 'abcd' ), '\n____________'
print laceStringsRecur('abcd',   ''     ), '\n____________'
print laceStringsRecur('',       '12345'), '\n____________'
print laceStringsRecur('',       ''     ), '\n____________'