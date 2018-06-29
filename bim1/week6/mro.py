class Shape(object):
    pass


class Plotter(object):
    pass


class Polygon(Shape, Plotter):
    pass


class RegularPolygon(Polygon):
    pass


class RegularHexagon(RegularPolygon):
    pass


class Square(RegularPolygon):
    pass


square = Square()
print(square.__class__.__mro__)
regularhexagon = RegularHexagon()
print(regularhexagon.__class__.__mro__)