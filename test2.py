import math

class quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.roots = []

    def discriminant(self):
        # Calculate the discriminant
        return self.b**2 - 4 * self.a * self.c

    def hasRealRoots(self):
        # Check if discriminant is non-negative
        return self.discriminant() >= 0

    def isFactorable(self):
        # Check if discriminant is a perfect square
        discriminant = self.discriminant()
        return discriminant >= 0 and math.isqrt(discriminant)**2 == discriminant

    def calcRoots(self):
        # Calculate roots if they are real
        if self.hasRealRoots():
            d = self.discriminant()
            root1 = (-self.b + math.sqrt(d)) / (2 * self.a)
            root2 = (-self.b - math.sqrt(d)) / (2 * self.a)
            self.roots = sorted([round(root1, 2), round(root2, 2)])
        return self.roots

    def axisOfSymmetry(self):
        # Calculate the x-coordinate of the axis of symmetry
        return -self.b / (2 * self.a)

    def vertex(self):
        # Calculate the vertex (x, y)
        x = self.axisOfSymmetry()
        y = self.a * x**2 + self.b * x + self.c
        return [round(x, 2), round(y, 2)]

class TextColor:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

if __name__ == "__main__":
    print("\033[94mQuadratic Equation Solver: ax^2 + bx + c = 0\033[0m")

    q1 = quadratic(1, 4, 4)
    assert q1.isFactorable() == True
    assert q1.hasRealRoots() == True
    assert q1.discriminant() == 0
    assert q1.calcRoots() == [-2, -2]
    assert q1.axisOfSymmetry() == -2
    assert q1.vertex() == [-2, 0]

    q2 = quadratic(1, 1, -6)
    assert q2.isFactorable() == True
    assert q2.hasRealRoots() == True
    assert q2.discriminant() == 25
    assert q2.calcRoots() == [-3, 2]
    assert q2.axisOfSymmetry() == -0.5
    assert q2.vertex() == [-0.5, -6.25]

    q3 = quadratic(1, 1, 10)
    assert q3.isFactorable() == False
    assert q3.hasRealRoots() == False
    assert q3.discriminant() == -39
    assert q3.calcRoots() == []
    assert q3.axisOfSymmetry() == -0.5

    q4 = quadratic(1, 10, 1)
    assert q4.isFactorable() == False
    assert q4.hasRealRoots() == True
    assert q4.discriminant() == 96
    assert q4.calcRoots() == [-9.9, -0.1]
    assert q4.axisOfSymmetry() == -5

    print("All assertions passed successfully.")
