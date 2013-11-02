__author__ = 'Sabin Purice'


balance = 3329
annualInterestRate = 0.2

#balance = 320000
#annualInterestRate = 0.2

b = balance
r = annualInterestRate

#b = int(raw_input('Ballance = '))
#r = float(raw_input('Anual Interest Rate = '))

total = 0
p = 180


def min_pay(b, p):
    """Returns Unpaid Balance after Payment"""
    ub = b - p
    ub += (r / 12.0) * ub
    return ub


def one_year(pay, total = total, b = b):
    """Calculates Balance after One Year"""
    for i in range(0, 12):
        total += p
        if i < 11:
            b = min_pay(b, pay)
    return min_pay(b, pay)

while one_year(p) > 0:
    p +=10

print('Lowest Payment: ' + str(p))
print('Payment after One Year: ' + str(one_year(p)))
