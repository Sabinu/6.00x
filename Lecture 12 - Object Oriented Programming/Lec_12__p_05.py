__author__ = 'Sabinu'


def genPrimes_mySolution():
    pn = [2]
    prime = 2
    while True:
        yield prime

        flag = False
        while flag is False:
            flag, prime = True, prime+1
            for p in pn:
                if prime % p == 0:
                    flag = False
        pn.append(prime)


def genPrimes():
    primes = []
    last = 1
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last