__author__ = 'Sabinu'


def laceStrings(s1, s2):
    """
    @param s1 : string
    @param s2 : string
    @return   : str with elements of s1 and s2 interlaced,
                beginning with s1. If strings are not of same length,
                then the extra elements should appear at the end.
    """
    run = min(len(s1), len(s2))
    result = ''
    for i in range(run):
        result += s1[i] + s2[i]
    if len(s1) > len(s2):
        result += s1[run:]
    else:
        result += s2[run:]
    return result

## TEST SUITE
print laceStrings('abcd',   '12345'), '\n____________'
print laceStrings('123456', 'abcd'),  '\n____________'
print laceStrings('abcd',   ''),      '\n____________'
print laceStrings('',       '12345'), '\n____________'
print laceStrings('',       ''),      '\n____________'