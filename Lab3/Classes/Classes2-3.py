class Shape:
    def __init__(self):
        self.ar = 0

    def area(self):
        return self.ar


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.ar = length ** 2


# # # # 3
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width * 2

s1 = Square(10)
s2 = Shape()
print(s1.area())
print(s2.area())
s3 = Rectangle(12, 6)
print(s3.area())