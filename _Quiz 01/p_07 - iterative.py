__author__ = 'Sabinu'

solutions = {}


def McNuggets(n):
    """
    @param n  : integer
    @return   : boolean
                True if some integer combination of 6, 9 and 20 equals n
                False Otherwise.
    """
    solutions[n] = []
    for a in range(n//6 + 1):
        for b in range(n//9 + 1):
            for c in range(n//20 + 1):
                if a*6 + b*9 + c*20 == n:
                    solutions[n].append([a, b, c])
    if len(solutions[n]) != 0:
        return True
    return False


for i in range(10, 50):
    McNuggets(i),

for i in solutions.items():
    print len(i[1]), i