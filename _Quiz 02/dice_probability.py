def probTest(limit):
    roll = 1
    up = 1
    down = 6

    while (up / float(down)) > limit:
        roll += 1
        up *= 5
        down *= 6
    
    lesser = round(up / float(down), 2)

    print('{}/{} = {} | < {}'.format(up, down, lesser, limit))

    return roll


print(probTest(.105))