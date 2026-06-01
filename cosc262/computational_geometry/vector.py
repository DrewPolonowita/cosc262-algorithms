class Vec:
    """A simple vector in 2D. Also used as a position vector for points"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    def __mul__(self, scale):
        return Vec(self.x * scale, self.y * scale)
    def dot(self, other):
        return self.x * other.x + self.y * other.y
    def lensq(self):
        return self.dot(self)
    def __repr__(self):
        return "({}, {})".format(self.x, self.y)