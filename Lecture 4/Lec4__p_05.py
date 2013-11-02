def clip(lo, x, hi):
    """
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    """
    x = max(lo,x)
    x = min(x,hi)
    return x

x = int(raw_input('x = '))
lo = int(raw_input('lo = '))
hi = int(raw_input('hi = '))
print('Clipped value = ' + str(clip(lo, x, hi)))