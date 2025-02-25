class Calculator:
    def sum(self, a, b, c=0):
        return a+b+c

calculator =  Calculator()
print(calculator.sum(7,9))
print(calculator.sum(6,9,5))
x=2
y=5
z = x + y
print(z)

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

c1 = Coordinate(6,9)
c2 = Coordinate(4,5)
c3 = c1 + c2
c4 = c1 - c2
print(c3)
print(c4)

