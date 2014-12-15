__author__ = 'Sabinu'


class Position(object):
    """ A Position represents a location in a two-dimensional room. """

    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):
        return "(%0.2f, %0.2f)" % (self.x, self.y)


class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty tiles.
    A room has a width and a height and contains (width * height) tiles.
    At any particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.
        width: an integer > 0
        height: an integer > 0
        """
        self.tiles = {}
        self.width = width
        self.height = height

        for i in range(width):
            for j in range(height):
                self.tiles[(i, j)] = False

    def __str__(self):
        out = ''
        for i in range(self.width):
            for j in range(self.height):
                out += str(int(self.tiles[(i, j)])) + ' '
            out += '\n'
        return out

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.
        pos: a Position
        """
        self.tiles[(int(pos.getX()), int(pos.getY()))] = True

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.
        Assumes that (m, n) represents a valid tile inside the room.
        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.tiles[(int(m), int(n))]

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.
        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.
        returns: an integer
        """
        clean = 0
        for v in self.tiles.values():
            clean += v
        return clean

    def getRandomPosition(self):
        """
        Return a random position inside the room.
        returns: a Position object.
        """
        # random.seed(0)
        w = random.randrange(self.width)
        h = random.randrange(self.height)

        return Position(w, h)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.
        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        x = pos.getX()
        y = pos.getY()
        return 0 <= x < self.width and \
               0 <= y < self.height

dim = 4

c = RectangularRoom(dim, dim)

print c

print '1st run:\n'
for i in range(dim):
    c.cleanTileAtPosition(Position(i, i))
    print c

print '2nd run:\n'
for i in range(dim):
    c.cleanTileAtPosition(Position(i, i))
    print c