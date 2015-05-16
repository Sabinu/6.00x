__author__ = 'Sabin'


# Rescrie chestia asta cu un output ordonat

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


def avv(lst):
    '''
    Returns the average of a list items.
    '''
    Su = 0
    for i in lst:
        Su += i

    return Su/len(lst)


def print_Ave(lst, i):
    print('Average for et. {} is: {:6.3f} :: List was {} elements long.'.format(i, round(avv(lst), 3), len(lst)))
    return None


def diff(lst):
    ''' Prints differences between list items. '''
    print()
    for i in range(len(lst)-1):
        print('Dif {}: {:5.3f}'.format(i+1, round(lst[i+1]-lst[i], 3)))
    return None


def dist_avv(lst):
    '''
    Calculates & Prints distance of list items from average of list.
    '''
    ind = 1
    print('')
    for i in lst:
        print('Member nr.{} is {:5.3f} far away from list average of {:6.3f}'.format(ind, round(abs(avv(lst)-i), 3), round(avv(lst), 3)))
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