import math

# ======================================= PVector ====================
# Represents a step in 2D space from one point to another.
# That is what a vector is.

class PVector:

    def __init__(self, x1, y1, x2, y2):

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @property
    def dx(self):
        
        return self.x2 - self.x1;

    @property
    def dy(self):
        
        return self.y2 - self.y1;

    @property
    def length_squared(self):
        
        return self.dx * self.dx + self.dy * self.dy

    @property
    def length(self):
        
        return math.sqrt(self.length_squared)

    def normalised(self):
        
        # returns a new direction vector of length 1.0 pointing the same direction as this vector
        my_length = self.length
        return PVector(0, 0, self.dx / my_length, self.dy / my_length)

    def perpendicular(self):
        
        # Produces a new direction vector of length 1.0 that is perpendicular to this one
        my_length = self.length
        return PVector(0, 0, self.dy / my_length, -self.dx / my_length)

    def faster_perpendicular(self):
        
        # Produces a new direction vector that is perpendicular to this one
        return PVector(0, 0, self.dy, -self.dx)

    def get_vector_to(self, x, y):
        
        # Produces a direction vector to the given point from this vectors (x1,y1)
        dx = x - self.x1
        dy = y - self.y1
        return PVector(0, 0, dx, dy)

    @staticmethod
    def scalar_multiply(vector1, vector2):
        
        # Scalar multiple of two vectors. Returns a number that is related to if they point in the same direction
        return vector1.dx * vector2.dx + vector1.dy * vector2.dy
        
    
        
        


