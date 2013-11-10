__author__ = 'Sabinu'


def McNuggets(n):
    """
    @param n  : integer
    @return   : boolean
                True if some integer combination of 6, 9 and 20 equals n
                False Otherwise.
    """
    for a in range(n//6 + 1):
        for b in range(n//9 + 1):
            for c in range(n//20 + 1):
                if a*6 + b*9 + c*20 == n:
                    #print [a, b, c],
                    return True
    #print [a, b, c],
    return False

#for i in [15, 16, 18, 28, 38, 27, 71]:
#    print i, McNuggets(i)

lst = []

for i in range(5000):
    if not McNuggets(i):
        lst.append(i)

print len(lst)
print lst
print McNuggets(44)