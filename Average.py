__author__ = 'Sabin'


def ave():
    '''
    Returns the average of a user input list.
    '''
    i = 1
    ave = []
    while True:
        e = input('Value ' + str(i) + ': ')
        if not e:
            break
        else:
            ave.append(float(e))
            i += 1
    Su = 0
    for i in ave:
        Su += i
    print('Average is: ' + str(Su/len(ave)))

    return Su/len(ave)


def avv(li5t):
    '''
    Returns the average of a list items.
    '''
    Su = 0
    for i in li5t:
        Su += i

    return Su/len(li5t)


def print_Ave(li5t, i):
    print('Average for et.' + str(i) + ' is: ' + str(round(avv(li5t), 3)) + ' :: List was ' + str(len(li5t)) + ' elements long.')
    return None


def diff(li5t):
    '''
    Prints differences between list items.
    '''
    for i in range(len(li5t)-1):
        print('\nDif ' + str(i+1) + ': ' + str(round(li5t[i+1]-li5t[i], 3)))
    return None


def dist_avv(li5t):
    '''
    Calculates & Prints distance of list items from average of list.
    '''
    ind = 1
    print('')
    for i in li5t:
        print('Member nr.' + str(ind) + ' is ' + str(round(abs(avv(li5t)-i), 3)) + ' far away from list average of ' + str(round(avv(li5t), 3)))
        ind +=1
    return None

et1 = [8.167, 8.174, 8.168, 8.168, 8.174, 8.169, 8.171]
et2 = [11.468, 11.471, 11.472, 11.478, 11.472, 11.480, 11.472]
et3 = [14.763, 14.765, 14.747, 14.737, 14.747, 14.759, 14.763, 14.774]
et4 = [18.247, 18.237, 18.237, 18.257, 18.241]

print('')
print_Ave(et1, 1)
print_Ave(et2, 2)
print_Ave(et3, 3)
print_Ave(et4, 4)

etaje = [avv(et1), avv(et2), avv(et3), avv(et4)]

diff(etaje)

dist_avv(et1)
dist_avv(et2)
dist_avv(et3)
dist_avv(et4)