def union(set1, set2):
    """
    set1 and set2 are collections of objects, each of which might be empty.
    Each set has no duplicates within itself, but there may be objects that
    are in both sets. Objects are assumed to be of the same type.

    This function returns one set containing all elements from
    both input sets, but with no duplicates.
    """
    if len(set1) == 0:
        return set2
    elif set1[0] in set2:
        return union(set1[1:], set2)
    else:
        return set1[0] + union(set1[1:], set2)


test_a = [('', ''), ('', 'a'), ('', 'ab'), ('a', ''), ('a', 'b'), ('c', 'ab'), ('de', ''), ('ab', 'c'), ('cd', 'ab')]
test_b = [('abc', ''), ('abc', 'a'), ('abc', 'ab'), ('abc', 'd'), ('abc', 'abcd')]
test_c = [('', 'abc'), ('a', 'abc'), ('ab', 'abc'), ('abc', 'abc')]
test_d = [('', 'abc'), ('a', 'abc'), ('ab', 'abc'), ('d', 'abc')]

teste = [test_a, test_b, test_c, test_d]

for i, t in enumerate(teste):
    print 'Test %s:' % (i+1)
    for tes in t:
        a, b = tes
        print union(a, b),
    print '\n'
