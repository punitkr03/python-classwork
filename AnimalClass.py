class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, length, width, name) -> None:
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
