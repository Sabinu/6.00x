__author__ = 'Sabinu'


def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string

    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if len(str1) == 1 or len(str2) == 0:
        if str1 == str2:
            return True
        return False
    elif str1[0] == str2[-1] and str1[-1] == str2[0]:
        return semordnilap(str1[1:-1], str2[1:-1])
    return False


def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)

print semordnilapWrapper('dog', 'god')
print semordnilapWrapper('evil', 'live')
print semordnilapWrapper('nametag', 'gateman')
print semordnilapWrapper('desserts', 'stressed')
print semordnilapWrapper('desserts', 's')
print semordnilapWrapper('desserts', 'stre/sed')
print semordnilapWrapper('dog', 'g/d')
