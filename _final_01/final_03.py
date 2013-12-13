__author__ = 'Sabinu'


def sort1(lst):
    swapFlag = True
    iteration = 0
    while swapFlag:
        swapFlag = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                temp = lst[i + 1]
                lst[i + 1] = lst[i]
                lst[i] = temp
                swapFlag = True

        L = lst[:]  # the next 3 questions below refer to this line
        iteration += 1
    return lst


def sort2(lst):
    for iteration in range(len(lst)):
        minIndex = iteration
        minValue = lst[iteration]
        for j in range(iteration + 1, len(lst)):
            if lst[j] < minValue:
                minIndex = j
                minValue = lst[j]
        temp = lst[iteration]
        lst[iteration] = minValue
        lst[minIndex] = temp

        L = lst[:]  # the next 3 questions below refer to this line
    return lst


def sort3(lst):
    out = []
    for iteration in range(len(lst)):
        new = lst[iteration]
        inserted = False
        for j in range(len(out)):
            if new < out[j]:
                out.insert(j, new)
                inserted = True
                break
        if not inserted:
            out.append(new)

        L = out[:]  # the next 3 questions below refer to this line
    return out


def sort4(lst):
    def unite(l1, l2):
        if len(l1) == 0:
            return l2
        elif len(l2) == 0:
            return l1
        elif l1[0] < l2[0]:
            return [l1[0]] + unite(l1[1:], l2)
        else:
            return [l2[0]] + unite(l1, l2[1:])

    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        front = sort4(lst[:len(lst)/2])
        back = sort4(lst[len(lst)/2:])

        L = lst[:]  # the next 3 questions below refer to this line
        return unite(front, back)


sort = [9, 3, 2, 4, 1, 5, 8, 7]

print sort4(sort)