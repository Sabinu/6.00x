import operator


def merge(left, right, compare):
    """
    Merge Algorithm.
    """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(L, compare=operator.lt):
    """
    Merge-Sort Algorithm.
    """
    global num
    print '===', num, L
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        num[0] += 1
        left = merge_sort(L[:middle], compare)
        num[1] += 1
        right = merge_sort(L[middle:], compare)
        print '++++++++++', left, right,
        print '>>>', merge(left, right, compare)
        return merge(left, right, compare)

print'___________________________'
lst = [1, 5, 8, 4, 3, 0, 2, 7, 6, 9]
num = [0, 0]
print lst
print merge_sort(lst)
print lst
