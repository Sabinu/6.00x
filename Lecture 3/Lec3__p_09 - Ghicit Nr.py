print('Please think of a number between 0 and 100!')

low = 0
high = 100
a = 'a'
guess = (low + high) /2

while a != 'c':
    print('Is your secret number ' + str(guess) + '?')
    a = raw_input('Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly. ')
    while a != 'l' and a != 'h'and a != 'c':
        print('>>> Sorry, I did not understand your input. <<<')
        print('Is your secret number ' + str(guess) + '?')
        a = raw_input('Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly. ')
    if a == 'l':
        low = guess
    elif a == 'h':
        high = guess
    guess = (low + high) /2

print(' ')
print('Game over. Your secret number was: ' + str(guess))
