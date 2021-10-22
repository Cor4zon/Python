# about super

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


    def perimetr(self):
        return 2 * self.width + 2 * self.length


class Square(Rectangle):
    def __int__(self, length):
        super().__init__(length, length)


