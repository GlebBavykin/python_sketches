from enum import Enum, auto


class Color(Enum):
    """
    Color for a shape
    """

    WITHOUT_COLOR = auto()
    RED = auto()
    WHITE = auto()
    BLACK = auto()
    YELLOW = auto()


class Shape:
    """
    Shape with color
    """

    def __init__(self, color: Color = Color.WITHOUT_COLOR):
        self.color = color

    def __repr__(self):
        pass


class Circle(Shape):
    """
    Concrete Circle shape with color
    """

    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def change_radius(self, new_radius):
        self.__radius = new_radius

    def __repr__(self):
        return f"Circle({self.__radius}, {self.color}) with {self.color} color"


class Rectangle(Shape):
    """
    Concrete Rectangle shape with color
    """

    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

    def change_width_and_height(self, new_width, new_height):
        self.__width = new_width
        self.__height = new_height

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height}) with {self.color} color"
