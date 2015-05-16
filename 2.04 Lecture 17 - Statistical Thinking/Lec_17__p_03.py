__author__ = 'Sabinu'


def stdDev(data):
    """ Standard Deviation """
    mean = sum(data) / float(len(data))
    total = 0.0
    for d in data:
        total += (d - mean) ** 2
    return (total / len(data)) ** 0.5


def stdDevOfLengths(L):
    """ L       :   a list of strings
        returns :   float - the standard deviation of the lengths of the strings,
                    NaN   - if L is empty.
    """
    if len(L) is 0:
        return float('NaN')

    data = []
    for l in L:
        data.append(len(l))

    mean = sum(data) / float(len(data))
    total = 0.0
    for d in data:
        total += (d - mean) ** 2
    return (total / len(data)) ** 0.5


print(stdDevOfLengths(['a', 'z', 'p']))
print(stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples']))