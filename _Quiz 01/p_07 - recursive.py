__author__ = 'Sabinu'

solutions = {}
index = 1
solutions[index] = []
solutions[index].append([0, 0, 0])

def McNuggets(n):
    """
    @param n  : integer
    @return   : boolean
                True if some integer combination of 6, 9 and 20 equals n
                False Otherwise.
    """

    global index
    if n > index:
        index = n
        solutions[index] = []
        solutions[index].append([0, 0, 0])

    if n == 0:
        if False in solutions[index]:
            solutions[index].remove(False)
        solutions[index].append(True)
        return True
    for i in (6, 9, 20):
        if n >= i and McNuggets(n-i):
            if i == 6:
                solutions[index][0][0] += 1
            if i == 9:
                solutions[index][0][1] += 1
            if i == 20:
                solutions[index][0][2] += 1
            return True
    if True not in solutions[index] and False not in solutions[index]:
        solutions[index].append(False)
    return False

for i in range(100):
    McNuggets(i+1),

for i in solutions.items():
    print i