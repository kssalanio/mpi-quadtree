import numpy
class Point:
    """A point located at (x,y) in 2D space.

    Each Point object may be associated with a payload object.

    """

    def __init__(self, x, y, payload=None):
        self.x, self.y = float(x), float(y)
        self.payload = payload
        

    def __repr__(self):
        return '{}: {}'.format(str(self), repr(self.payload))

    def __str__(self):
        return f'P({self.x:.2f}, {self.y:.2f})'

    def distance_to(self, other):
        """ Compute the Euclidean distance to other point"""
        try:
            other_x, other_y = other.x, other.y
        except AttributeError:
            other_x, other_y = other
        return numpy.hypot(self.x - other_x, self.y - other_y)


