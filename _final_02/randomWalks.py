import random
import pylab


class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5

    def __repr__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'


class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


class Drunk(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return 'This drunk is named ' + self.name


class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [( 0.0,  1.0), ( 0.0, -1.0),
                       ( 1.0,  0.0), (-1.0,  0.0)]
        return random.choice(stepChoices)


class DiagonalDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(-1.0, -1.0), (-1.0,  0.0),
                       (-1.0,  1.0), ( 0.0,  1.0),
                       ( 0.0, -1.0), ( 1.0, -1.0),
                       ( 1.0,  0.0), ( 1.0,  1.0)]
        return random.choice(stepChoices)


class Weird_Field(Field):
    def __init__(self, leftEdge, rightEdge, bottomEdge, topEdge):
        self.drunks = {}
        self.leftEdge = leftEdge
        self.rightEdge = rightEdge
        self.bottomEdge = bottomEdge
        self.topEdge = topEdge

    def run_simulation(self, numSteps, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        origin = self.drunks[drunk]
        x, y = origin.getX(), origin.getY()
        x_pos, y_pos = [x], [y]
        for s in range(numSteps):
            self.moveDrunk(drunk)
            position = self.drunks[drunk]
            # print(position)
            x, y = position.getX(), position.getY()
            x_pos.append(x)
            y_pos.append(y)
        name = drunk.name
        pylab.figure('{}'.format(self.__class__.__name__))
        pylab.plot(x_pos, y_pos, 'b+', label=name)
        pylab.title('{} Drunk: {} timesteps'.format(name, numSteps))
        # pylab.xlabel('')
        # pylab.ylabel('')
        box_x = [self.leftEdge, self.leftEdge, self.rightEdge,
                 self.rightEdge, self.leftEdge]
        box_y = [self.topEdge, self.bottomEdge, self.bottomEdge,
                 self.topEdge, self.topEdge]
        pylab.plot(box_x, box_y, 'k-', label='limits')
        pylab.xlim([self.leftEdge - 10, self.rightEdge + 10])
        pylab.ylim([self.bottomEdge - 10, self.topEdge + 10])
        pylab.legend(loc='best')


class SW_Field(Weird_Field):
    """ SW (Solid Walls):
        The drunk cannot go through the fence.
        If the drunk sees that his move will make him run into the fence,
        the drunk will hesitate and not move from the spot.
    """
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        dx, dy = drunk.takeStep()
        position = self.drunks[drunk]
        x, y = position.getX(), position.getY()
        if x + dx > self.leftEdge and x + dx < self.rightEdge:
            x += dx
        if y + dy > self.bottomEdge and y + dy < self.topEdge:
            y += dy
        self.drunks[drunk] = Location(x, y)


class SP_Field(Weird_Field):
    """ SP (Small Planet):
        The rightmost edge is connected to the leftmost edge,
        and the top edge is connected to the bottom edge.
    """
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        dx, dy = drunk.takeStep()
        position = self.drunks[drunk]
        x, y = position.getX(), position.getY()
        # print(x, dx, self.leftEdge, '<', x + dx, '<', self.rightEdge)
        if (x + dx) > self.leftEdge and (x + dx) < self.rightEdge:
            x += dx
        elif (x + dx) >= self.rightEdge:
            x = self.leftEdge + (x + dx - self.rightEdge)
        elif (x + dx) <= self.leftEdge:
            x = self.rightEdge - (self.leftEdge - (x + dx))

        if (y + dy) > self.bottomEdge and (y + dy) < self.topEdge:
            y += dy
        elif (y + dy) >= self.topEdge:
            y = self.bottomEdge + (y + dy - self.topEdge)
        elif (y + dy) <= self.bottomEdge:
            y = self.topEdge - (self.bottomEdge - (y + dy))
        self.drunks[drunk] = Location(x, y)


class WW_Field(Weird_Field):
    """ WW (Warped World):
        If the drunk moves past the right-most edge,
        he ends up on the top edge and vice versa.
        If the drunk moves past the left edge,
        he ends up on the bottom edge and vice versa.
    """
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        dx, dy = drunk.takeStep()
        position = self.drunks[drunk]
        x, y = position.getX(), position.getY()
        if (x + dx) > self.leftEdge and (x + dx) < self.rightEdge and (y + dy) > self.bottomEdge and (y + dy) < self.topEdge:
            x += dx
            y += dy
        else:
            x, y = y, x
        self.drunks[drunk] = Location(x, y)


class BH_Field(Weird_Field):
    """ BH (Back to Home):
        Whenever the drunk reaches any edge,
        the drunk is transported back to the center of the world.
    """
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        dx, dy = drunk.takeStep()
        position = self.drunks[drunk]
        x, y = position.getX(), position.getY()
        if (x + dx) > self.leftEdge and (x + dx) < self.rightEdge and (y + dy) > self.bottomEdge and (y + dy) < self.topEdge:
            x += dx
            y += dy
        else:
            x = self.leftEdge + (self.rightEdge - self.leftEdge)/2
            y = self.bottomEdge + (self.topEdge - self.bottomEdge)/2
        self.drunks[drunk] = Location(x, y)

if __name__ == '__main__':
    # bro = UsualDrunk('Bro')
    bro = DiagonalDrunk('Bro')
    origin = Location(0.0, 0.0)

    sw_field = SW_Field(-50, 50, -50, 50)
    sw_field.addDrunk(bro, origin)
    sw_field.run_simulation(15000, bro)

    sp_field = SP_Field(-50, 50, -50, 50)
    sp_field.addDrunk(bro, origin)
    sp_field.run_simulation(15000, bro)

    ww_field = WW_Field(-50, 50, -50, 50)
    ww_field.addDrunk(bro, origin)
    ww_field.run_simulation(15000, bro)

    bh_field = BH_Field(-50, 50, -50, 50)
    bh_field.addDrunk(bro, origin)
    bh_field.run_simulation(15000, bro)

    pylab.show()
