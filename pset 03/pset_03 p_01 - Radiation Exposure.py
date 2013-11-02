__author__ = 'Sabinu'


def f(x):
    import math
    return 10 * math.e**(math.log(0.5) / 5.27 * x)


def radiationExposure(start, stop, step):
    """
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start:  integer, the time at which exposure begins
    stop:   integer, the time at which exposure ends
    step:   float, the width of each rectangle. You can assume that
            the step size will always partition the space evenly.

    returns:float, the amount of radiation exposed to
            between start and stop times.
    """
    total_radiation = 0
    roll = start
    while roll < stop:
        total_radiation += f(roll) * step
        roll += step
    return total_radiation

print 'Test Case 1: ', radiationExposure(0, 5, 1)
print 'Test Case 2: ', radiationExposure(5, 11, 1)
print 'Test Case 3: ', radiationExposure(0, 11, 1)
print 'Test Case 4: ', radiationExposure(40, 100, 1.5)