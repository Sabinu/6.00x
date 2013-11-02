__author__ = 'Sabinu'

# Call-Back Functions
def my_callback(inp):
    print "Function my_callback was called with %s input" % (inp,)


def caller(inp, func):
    func(inp)


for i in range(5):
    caller(i, my_callback)


# Fibonacci numbers, imperative style
def fibonacci(iterations):
    theSum, first, second = 0, 0, 1  # initial seed values
    for i in range(iterations - 1):  # Perform the operation iterations - 1 times.
        theSum = first + second
        first = second
        second = theSum  # Assign all the new values.
    return first  # Return the value when done.