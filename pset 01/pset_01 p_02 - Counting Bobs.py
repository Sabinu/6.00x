__author__ = 'Sabinu'

s = 'azcbobobegghakl'

b = 0

for i in range(len(s) - 2):
    if s[i: i+3] == 'bob':
        b += 1
print 'Number of times bob occurs: ' + str(b)

