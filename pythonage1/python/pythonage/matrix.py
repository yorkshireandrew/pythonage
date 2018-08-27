import math

# ===================== PMatrix ============
# Matrix Representing a position and orientation

class PMatrix:

    def __init__(self, a11, a12, a13, a21, a22, a23):
        self.a11 = a11 # Ratio of how much a change of x on the object results in a change of x on the screen
        self.a12 = a12 # Ratio of how much a change of y on the object results in a change of x on the screen
        self.a13 = a13 # The starting x position of the object on the screen
        self.a21 = a21 # Ratio of how much a change of y on the object results in a change of x on the screen
        self.a22 = a22 # Ratio of how much a change of y on the object results in a change of y on the screen
        self.a23 = a23 # The starting y position of the object on the screen

    @staticmethod
    def unity():
        return PMatrix(1.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    def translated(self, x, y):
        #a13 = self.a13 + x
        #a23 = self.a23 + y

        t_matrix = PMatrix(1.0, 0.0, x, 0.0, 1.0, y)
        return PMatrix.multiply(self, t_matrix)
        
        #return PMatrix(self.a11, self.a12, a13, self.a21, self.a22, a23)

    def rotated(self, angle):
        radians = math.radians(angle)
        b11 = math.cos(radians)
        b12 = -math.sin(radians)
        b13 = 0.0
        b21 = math.sin(radians)
        b22 = math.cos(radians)
        b23 = 0.0
        
        b_matrix = PMatrix(b11, b12, b13, b21, b22, b23)
        
        return PMatrix.multiply(self, b_matrix)
        
    @staticmethod
    def multiply(a,b):
        a11 = a.a11 * b.a11 + a.a12 * b.a21
        a12 = a.a11 * b.a12 + a.a12 * b.a22
        a13 = a.a11 * b.a13 + a.a12 * b.a23 + a.a13

        a21 = a.a21 * b.a11 + a.a22 * b.a21
        a22 = a.a21 * b.a12 + a.a22 * b.a22
        a23 = a.a21 * b.a13 + a.a22 * b.a23 + a.a23

        return PMatrix(a11, a12, a13, a21, a22, a23)

    def screen_x_of(self, x, y):
        return self.a11 * x + self.a12 * y + self.a13

    def screen_y_of(self, x, y):
        return self.a21 * x + self.a22 * y + self.a23

        

