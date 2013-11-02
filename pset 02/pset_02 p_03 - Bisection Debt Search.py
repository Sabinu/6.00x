__author__ = 'Sabin Purice'

balance = 320000
annualInterestRate = 0.2

b = balance
r = annualInterestRate


#b = int(raw_input('Ballance = '))
#r = float(raw_input('Anual Interest Rate = '))


def one_year(b, p):

    total = 0
    p = p

    def ub_pay(b, p):
        """
        Returns Unpaid Balance after Payment / per Month
        """
        ub = b - p
        ub += (r / 12.0) * ub
        return ub

    for i in range(0, 12):
        total += p
        if i < 11:
            b = ub_pay(b, p)
    return ub_pay(b, p)


def lowest_year(t):
    """
    >> Bisection Search
    calculates lowest payment for paying all in one year
    @rtype : float
    """
    lo_b = b / 12
    hi_b = one_year(b, 0) / 12

    p = (lo_b + hi_b) / 2

    while abs(one_year(b, p)) > t:
        if one_year(b, p) > 0:
            lo_b = p
        else:
            hi_b = p
        p = (lo_b + hi_b) / 2
    return p

pay = lowest_year(0.0001)
print('Lowest Payment:     ' + str(round(pay, 2)))
print('Payment after One Year: ' + str(one_year(b, pay)))