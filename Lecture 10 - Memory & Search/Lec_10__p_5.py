# Lecture 10 - Problem 5

def sel_sort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp
        print(L)
    return None


def new_sort(L):
    for i in range(len(L) - 1):
        j = i + 1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
        print(L)
    return None

# 01. Do the functions result in the same sorted list?
#     Yes
# 02. Do they execute the same nr. of assignments?
#     No. new_sort may use more but never fewer than sel_sort
# 03. Is the worst-case order of growth the same?
#     Yes. O(len(L)^2)

print'___________________________'
lst = [1, 5, 8, 4, 3, 0, 2, 7, 6]
sel_sort(lst)
print'___________________________'
lst = [1, 5, 8, 4, 3, 0, 2, 7, 6]
new_sort(lst)