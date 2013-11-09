__author__ = 'Sabinu'


def FancyDivide(list_of_numbers, index):
    denom = list_of_numbers[index]
    return [SimpleDivide(item, denom) for item in list_of_numbers]


#def SimpleDivide(item, denom):
#    return item / denom

def SimpleDivide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0

print FancyDivide([0, 2, 4], 0)  # << Problema
print FancyDivide([0, 2, 4], 1)
print FancyDivide([0, 2, 4], 2)