# Lec 2.6, slide 4

x = int(raw_input('Number to check if divisible by 2 or 3: '))

if x % 2 == 0:
    if x % 3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x % 3 == 0:
    print('Divisible by 3 and not by 2')
else:
    print('Not divisible by 2 or 3')
