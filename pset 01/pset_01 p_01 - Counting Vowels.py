__author__ = 'Sabinu'

s = 'azcbobobegghakl'

vowels = 'aeiou'
v = 0

for l in s:
    if l in vowels:
        v +=1
print 'Number of vowels: ' + str(v)