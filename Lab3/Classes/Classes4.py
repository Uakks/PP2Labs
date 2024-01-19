import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"x = {self.x}, y = {self.y}")

    def move(self, a, b):
        self.x = a
        self.y = b
        return self

    def dist(self, p1):
        print(math.sqrt((p1.x - self.x) ** 2 + (p1.y - self.y) ** 2))

q1 = Point(12, 4)
q2 = Point(5, 7)
q2.show()
q3 = q1.move(8, 9)
q2.dist(q1)
q3.show()
