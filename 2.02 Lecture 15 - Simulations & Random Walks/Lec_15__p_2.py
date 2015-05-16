import random

print(random.randint(1, 5))
print(random.choice(['apple', 'banana', 'cat']))
print('=' * 60)


def getEven():
    """
    Generates a random number x.
    Where 0 <= x < 100
    """
    return random.choice(range(0, 100, 2))

for i in range(10):
    print(getEven(),)