def search(L, e):
    for i in range(len(L)):
        print L[i]
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def newsearch(L, e):
    size = len(L)
    for i in range(size):
        print L[size-i-1], L[i]
        if L[size-i-1] == e:
            return True
        if L[i] < e:  # <<< Major mistake [size-i-1] - consistenta
            return False
    return False

L = [1, 3, 4, 5, 6, 9, 11]

print search(L, 4)
print newsearch(L, 4)