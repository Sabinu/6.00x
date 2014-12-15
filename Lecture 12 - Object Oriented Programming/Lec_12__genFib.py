__author__ = 'Sabinu'


def gen_fib():
    fibn_1 = 0
    fibn_2 = 1
    while True:
        next = fibn_1 + fibn_2
        yield next
        fibn_1, fibn_2 = fibn_2, next

print gen_fib().next()
print gen_fib().next()