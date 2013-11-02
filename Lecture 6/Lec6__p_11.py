__author__ = 'Sabinu'

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    bigg = 0
    result = None
    for i in aDict.keys():
        if len(aDict[i]) >= bigg:
            bigg = len(aDict[i])
            result = i
    return result

print biggest(animals)

