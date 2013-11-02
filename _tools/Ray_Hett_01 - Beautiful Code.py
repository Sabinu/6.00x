import argparse
from collections import defaultdict, namedtuple
import doctest
import os

__author__ = 'Sabinu'

names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

'''
for i in [0, 1, 2, 3, 4, 5]:
    print i**2

for i in range(6):
    print i**2

for i in xrange(6):  # produces values one at a time; in py3 it's just range
    print i**2

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Looping through a collection

for i in range(len(colors)):
    print colors[i]

# Do This
for color in colors:
    print color

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Loop Backwards

for i in range(len(colors)-1, -1, -1):
    print colors[i]

for color in reversed(colors):
    print color

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Loop over a collection and indicies

for i in range(len(colors)):
    print i, '-->', colors[i]

for i, color in enumerate(colors):
    print i, '-->', color

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Loop over two collections at once

n = min(len(names), len(colors))
for i in range(n):
    print(names[i], '-->', colors[i])

for name, color in zip(names, colors):  # Too much memory
    print(name, '-->', color)

# for name, color in izip(names, colors):  # Better; dunno where it works
#     print(name, '-->', color)

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Loop in sorted order

for color in sorted(colors):
    print color

for color in sorted(colors, reverse=True):
    print color

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Custom sort order


def compare_length(c1, c2):
    if len(c1) < len(c2):
        return -1
    if len(c1) > len(c2):
        return 1
    return 0

print sorted(colors, cmp=compare_length) # No longer valid in py3

# Do This
print sorted(colors, key=len) # A ton better

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Call a function until a sentinel value

blocks = []
while True:
    block = f.read(32)
    if block == '':
        break
    blocks.append(block)

blocks = []
for block in iter(partial(f.read, 32), ''):  # Where do I Get partial
    blocks.append(block)

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Distinguishing multiple exit points in loops


def find_1(seq, target):
    found = False
    for i, value in enumerate(seq):
        if value == target:
            found = True
            break
    if not found:
        return -1
    return i


def find_2(seq, target):
    for i, value in enumerate(seq):  # Every for loop has an 'else' inside == I finished the loop
        if value == target:
            break
    else:
        return -1
    return i

# Lamda '=' Make function

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Loop over dictionary keys

for k in d:
    print k

for k in d.keys():  # if you mutate the dictionary, makes a copy of the keys
    if k.startswith('r'):
        del d[k]

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Loop over dictionary keys & values

for k in d:
    print k, '-->', d[k]

for k, v in d.items():
    print k, '-->', v

for k, v in d.iteritems():
    print k, '-->', v

print d.items()
print d.iteritems()

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Construct a dictionary from pair

d_1 = dict(zip(names, colors))

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Count with a dictionary

colors_2 = ['red', 'green', 'red', 'blue', 'green', 'red']
d_1 = {}
for color in colors_2:
    if color not in d_1:
        d_1[color] = 0
    d_1[color] += 1

d_2 = {}
for color in colors_2:
    d_2[color] = d_2.get(color, 0) + 1

d_3 = defaultdict(int)
for color in colors_2:
    d[color] += 1

print d_1
print d_2
print d_3

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Grouping with dictionaries -- Part I

names_1 = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']

d_4 = {}
for name in names_1:
    key = len(name)
    if key not in d_4:
        d_4[key] = []
    d_4[key].append(name)

print d_4
# = {5: ['roger', 'betty'], 6: ['rachel', 'judith'], 7: ['raymond', 'matthew', 'melissa', 'charlie']}

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Grouping with dictionaries

names_2 = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']

d_5 = {}
for name in names_2:
    key = len(name)
    d_5.setdefault(key, []).append(name)

d_6 = defaultdict(list)
for name in names_2:
    key = len(name)
    d_6[key].append(name)

print d_5
print dict(d_6)
# = {5: ['roger', 'betty'], 6: ['rachel', 'judith'], 7: ['raymond', 'matthew', 'melissa', 'charlie']}

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Is a dictionary popitem() atomic?

d_7 = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

while d_7:
    key, value = d_7.popitem()
    print key, '-->', value

print d_7  # Empty dictionary

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Linking Dictionaries

defaults = {'color': 'red', 'user': 'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args([])
command_line_args = {k: v for k, v in vars(namespace).items() if v}

#  A lot of Copying
d_8 = defaults.copy()
d_8.update(os.environ)
d_8.update(command_line_args)

# d_9 = ChainMap(command_line_args, os.environ, defaults)  # only in py3

for i, e in d_8.items:
    print i, '-->', e
print d_8

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Clarify funcion calls with keyword arguments

# Not like this >>> twitter_search('@obama', False, 20, True)
# Like this     >>> twitter_search('@obama', retweets=False, numtweets=20, popular=True)

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Clarify multiple return values with ''named tuples''

# print doctest.testmod()

TestResults = namedtuple('TestResults', ['failed', 'attempted'])
my_test = TestResults(failed=1, attempted=3)
print TestResults, '\n', my_test

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Unpacking sequences

p = ['Raymond', 'Hettinger', 0x30, 'python@example.com']

#fname = p[0]
#lname = p[1]
#age = p[2]
#email = p[3]
#print fname, lname, age, email

fname, lname, age, email = p
print fname, lname, age, email

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Updating multiple state variables


def fibonacci_1(n):  # NOT LIKE THIS
    x = 0
    y = 1
    for i in range(n):
        print x
        t = y
        y += x
        x = t


def fibonacci_2(n):  # LIKE THIS
    x, y = 0, 1
    for i in range(n):
        print x
        x, y = y, x + y

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Simultaneous state updates: Planet orbits

tmp_x = x + dx * t
tmp_y = y + dy * t
tmp_dx = influence(m, x, y, dx, dy, partial='x')
tmp_dy = influence(m, x, y, dx, dy, partial='y')
x = tmp_x
y = tmp_y
dx = tmp_dx
dy = tmp_dy

x, y, dx, dy = (x + dx * t,
                y + dy * t,
                influence(m, x, y, dx, dy, partial='x'),
                influence(m, x, y, dx, dy, partial='y'))

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## Concatenating strings
'''

names_3 = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']

s = names_3[0]
for name in names_3[1:]:
    s += ', ' + name
print s

print ', '.join(names_3)

# Minute 38