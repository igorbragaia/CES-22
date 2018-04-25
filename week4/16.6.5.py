import sys


def test(did_pass):
    """
    Prints test result
    :param did_pass: test result
    :return:
    """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y


class Rectangle:
    """ A class to manufacture rectangle objects"""

    def __init__(self, posn, w, h):
        """ Initiate rectangle at posn Point, with width w, height h"""
        self.corner = posn
        self.width = w
        self.height = h

    def collide(self, rect2):
        """
        Checks if current rect and rect2 collides
        :param rect2: Rectangle object
        :return: boolean
        """
        return (self.pointInsideCheck(rect2.corner) or
                self.pointInsideCheck(Point(rect2.corner.x + rect2.height, rect2.corner.y)) or
                self.pointInsideCheck(Point(rect2.corner.x, rect2.corner.y + rect2.width)) or
                self.pointInsideCheck(Point(rect2.corner.x + rect2.height, rect2.corner.y + rect2.width)))

    def pointInsideCheck(self, point):
        """
        checks if a point is inside current rect
        :param point: Point object
        :return: boolean
        """
        return (point.y >= self.corner.y and point.y <= self.corner.y + self.width and
                point.x >= self.corner.x and point.x <= self.corner.x + self.height)

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)


print(Rectangle(Point(0, 0), 100, 200).collide(Rectangle(Point(100, 101), 5, 10)))
print(Rectangle(Point(0, 0), 100, 200).collide(Rectangle(Point(100, 99), 5, 10)))
