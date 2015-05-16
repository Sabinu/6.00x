index = 0


def getPermutations(string):
    # Mock-up of RECURSIVE YIELD METHOD
    global index
    index += 1
    if len(string) == 1:
        print('final : {} {}'.format(index, string))
        yield string
    else:
        for i in range(len(string)):
            print('> {}+{} <'.format(string[:i], string[i+1:]))
            for num, perm in enumerate(getPermutations(string[:i] + string[i+1:])):
                print('inside: {} {} {}'.format(index, num, perm))
                yield string[i] + perm


for p in getPermutations('abc'):
    print('>>>>>>>>>>>>>>>>>>>>> {}'.format(p))