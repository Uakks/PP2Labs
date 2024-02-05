import math


class My_Shape:
    def __init__(self, color='blue', is_filled=True):
        self.color = color
        self.is_filled = is_filled

    def __str__(self):
        return f'Current color - {self.color}'

    def getArea(self):
        return 0


class Rectangle(My_Shape):
    def __init__(self, x_top_left, y_top_left, length, width):
        super().__init__('')
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

    def __str__(self):
        return (f'Rectangle has length - {self.length}, and width - {self.width}. '
                f'Top-left corner at ({self.x_top_left}, {self.y_top_left}), '
                f'so the area is {self.getArea()}')


class Circle(My_Shape):
    def __init__(self, x_center, y_center, radius):
        super().__init__('')
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius**2

    def __str__(self):
        return f'Circle has radius of {self.radius}, center is ({self.x_center}, {self.y_center})'


x = int(input('Enter a x coordinate: '))
y = int(input('Enter a y coordinate: '))
leng = int(input('Enter the length of the rectangle: '))
wid = int(input('Enter the width of the rectangle: '))
my_rectangle = Rectangle(x, y, leng, wid)
print(my_rectangle)
