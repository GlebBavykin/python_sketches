import math


class RoundPeg:
    """
    Compatible Peg with RoundHole
    """

    def __init__(self, radius: float, length: float):
        self._radius = radius
        self._length = length

    @property
    def radius(self):
        return self._radius

    @property
    def length(self):
        return self._length


class SquarePeg:
    """
    Incompatible Peg with RoundHole
    """

    def __init__(self, width: float, length: float):
        self._width = width
        self._length = length

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length


class RoundHole:
    """
    A RoundHole
    """

    def __init__(self, radius: float, height: float):
        self._radius = radius
        self._height = height

    @property
    def radius(self):
        return self._radius

    @property
    def height(self):
        return self._height

    def fits(self, peg: RoundPeg):
        return self.radius > peg.radius and self.height > peg.length


class SquarePegAdapter(RoundPeg):
    """
    Adapter to make SquarePeg compatible with RoundHole
    """

    def __init__(self, square_peg: SquarePeg):
        self._square_peg = square_peg

    @property
    def radius(self):
        return self._square_peg.width * (math.sqrt(2) / 2)

    @property
    def length(self):
        return self._square_peg.length
