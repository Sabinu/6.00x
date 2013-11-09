__author__ = 'Sabinu'

def Normalize_1(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers


try:
    Normalize_1([0, 0, 0])
except ZeroDivisionError, e:
    print 'Invalid maximum element'


def Normalize_2(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers


Normalize_2([0, 0, 0])