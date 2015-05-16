# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


def yieldAllCombos(items):
    """ Generates all combinations of N items into two bags,
        whereby each item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is
        represented as list of which item(s) in each bag.
    """
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        combo_lst_1 = []
        combo_lst_2 = []
        # test base(3) j'th of integer i
        base3_combo = make_tribit(i, N)
        # print(base3_combo)
        for j in range(N):
            if base3_combo[j] == '1':
                combo_lst_1.append(items[j])
            if base3_combo[j] == '2':
                combo_lst_2.append(items[j])
        yield (combo_lst_1, combo_lst_2)


def make_tribit(number, length):
    """ Transforms decimal base(10) system number to a
        0, 1, 2 base(3) system | extended to length
    """
    result = ''
    remainder = number
    while remainder != 0:
        result = str(remainder % 3) + result
        remainder = remainder // 3
    while len(result) < length:
        result = '0' + result
    return result

if __name__ == '__main__':
    # for i in powerSet([1, 2, 3]):
        # print(i)
    for i in yieldAllCombos([1, 2, 3]):
        print(i)
