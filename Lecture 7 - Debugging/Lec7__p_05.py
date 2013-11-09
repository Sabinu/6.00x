def foo(x, a):
    """
    x: a positive integer argument
    a: a positive integer argument

    returns an integer
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count


test_a = [(  2, 5), ( 5, 6), ( 9, 7)]
test_b = [( 10, 3), ( 1, 4), (10, 6)]
test_c = [(100, 5), (96, 5), (22, 5)]

teste = [test_a, test_b, test_c]

for i, t in enumerate(teste):
    print 'Test %s:' % (i+1)
    for tes in t:
        a, b = tes
        print foo(a, b),
    print '\n'