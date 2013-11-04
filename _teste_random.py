def fib(n):
    """
    @param n : number of fib numbers
    @rtype   : list
    @return  : list of fib numbers
    """
    lst = []
    if n > 0:
        lst.append(1)
    if n > 1:
        lst.append(1)
    n -= 2
    for i in range(n):
        lst.append(lst[i] + lst[i+1])

    return lst

print 'Suma:', sum(fib(6))
print fib(6)