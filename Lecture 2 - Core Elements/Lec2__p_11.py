varA = input('varA = ')
varB = input('varB = ')

if type(varA) == str or type(varB) == str:
    print('string involved')
else:
    if varA > varB:
        print('bigger')
    elif varA == varB:
        print('equal')
    elif varA < varB:
        print('smaller')
