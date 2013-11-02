__author__ = 'Sabin Purice'

#balance = 4842
#anualInterestRate = 0.2
#monthlyPaymentRate = 0.04

#b = balance
#r = annualInterestRate
#m = monthlyPaymentRate

b = int(raw_input('Ballance = '))
r = float(raw_input('Anual Interest Rate = '))
m = float(raw_input('Monthly Payment Rate = '))

total = 0


def min_pay(b, p):
    ub = b - p
    ub += (r / 12.0) * ub
    return ub

p = b * m

for i in range(0, 12):
    total += p
    print('Month: ' + str(i+1))
    print('Minimum monthly payment: ' + str(round(p, 2)))
    print('Remaining balance: ' + str(round(min_pay(b, p), 2)))
    if i < 11:
        b = min_pay(b, p)
        p = b * m

print('Total paid: ' + str(round(total, 2)))
print('Remaining balance: ' + str(round(min_pay(b, p), 2)))