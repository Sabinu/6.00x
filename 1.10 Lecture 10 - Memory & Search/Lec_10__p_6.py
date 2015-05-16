# Lecture 10 - Problem 5


def my_sort(L):
    """
    @param L: list
    @return : None
    
    Bubble sort algorithm.
    Modifies List.
    """
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                print (L[j-1], L[j]),
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
        print ''
    return None


def new_sort(L):
    for i in range(len(L) - 1):
        j = i + 1
        while j < len(L):
            if L[i] > L[j]:
                print (L[i], L[j]),
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
        print ''
    return None

# 01. Do the functions result in the same sorted list?
#     Yes.
# 02. Do they execute the same nr. of assignments?
#     Yes.
# 03. Is the worst-case order of growth the same?
#     Yes. O(len(L)^2)
# 04. Do they examine the same nr. of entries in the list?
#     No. my_sort examines more than new_sort

print'___________________________'
lst = [1, 5, 8, 4, 3, 0, 2, 7, 6]
my_sort(lst)
print'___________________________'
lst = [1, 5, 8, 4, 3, 0, 2, 7, 6]
new_sort(lst)