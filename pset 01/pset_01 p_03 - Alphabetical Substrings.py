__author__ = 'Sabinu'
## Determina cel mai lung sir de litere
## in ordine alfabetica dintr-un sir


s = 'azcbobobegghaklabcdef'
#s = 'vknidbwatwnnfzbsfff'
#s = 'abcdefghijklmnopqrstuvwxyz'

lngst = ''

pas = 0
while pas < len(s) - 1:
    cut = s[pas]
    while s[pas] <= s[pas + 1]:
        cut += s[pas + 1]
        pas += 1
        if pas == len(s)-1:
            break
    if len(cut) > len(lngst):
        lngst = cut
    pas += 1

print('Longest: ' + lngst)