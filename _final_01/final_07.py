__author__ = 'Sabinu'


class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None

    def setBefore(self, before):
        self.before = before

    def setAfter(self, after):
        self.after = after

    def getBefore(self):
        return self.before

    def getAfter(self):
        return self.after

    def myName(self):
        return self.name


def print_list(sFrob):
    while sFrob.getBefore():
        sFrob = sFrob.getBefore()
    print '\nLIST :', sFrob.myName(),
    while sFrob.getAfter():
        sFrob = sFrob.getAfter()
        print '<', sFrob.myName(),
    print ''


def insert(atMe, newFrob):
    """
    atMe    : a Frob that is part of a doubly linked list
    newFrob : a Frob with no links
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.
    """
    if newFrob.myName() < atMe.myName():
        if atMe.getBefore() is None:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        elif atMe.getBefore().myName() < newFrob.myName():
            before = atMe.getBefore()
            after  = atMe

            newFrob.setBefore(before)
            newFrob.setAfter(after)

            before.setAfter(newFrob)
            atMe.setBefore(newFrob)

        else:
            insert(atMe.getBefore(), newFrob)

    else:
        if atMe.getAfter() is None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        elif newFrob.myName() < atMe.getAfter().myName():
            before = atMe
            after  = atMe.getAfter()

            newFrob.setBefore(before)
            newFrob.setAfter(after)

            atMe.setAfter(newFrob)
            after.setBefore(newFrob)
        else:
            insert(atMe.getAfter(), newFrob)


def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list
    """
    if start.getBefore():
        return findFront(start.getBefore())
    else:
        return start

eric    = Frob('eric')
andrew  = Frob('andrew')
ruth    = Frob('ruth')
fred    = Frob('fred')
martha  = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)


print_list(eric)

print 'FRONT:', findFront(ruth).myName()