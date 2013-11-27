__author__ = 'Sabinu'

x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    print guess,
    if guess <= x:
        guess += step
        print guess
    else:
        break

print ''
if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))