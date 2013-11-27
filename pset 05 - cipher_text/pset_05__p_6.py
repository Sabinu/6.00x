##  Problem 6-1
def swapSort(L):
    """ L is a list on integers """
    print "O: \t", L
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                L[j], L[i] = L[i], L[j]
                print '\t', L, i, j
    print "F: \t", L


def modSwapSort(L):
    """ L is a list on integers """
    print "O: \t", L
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                L[j], L[i] = L[i], L[j]
                print '\t', L, i, j
    print "F: \t", L


L = [2, 5, 4, 6, 1, 3, 7, 9, 8, 0]
#L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

swapSort(L)
modSwapSort(L)