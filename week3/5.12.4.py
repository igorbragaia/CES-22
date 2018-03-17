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

    def get_line_to(self, point):
        if point.x == self.x and point.y == self.y:
            raise Exception("Same two points do not define a line")

        m = (self.y - point.y) / (self.x - point.x)
        c = self.y - self.x * m

        return m, c


test(Point(4, 11).get_line_to(Point(6, 15)) == (2, 3))
test(Point(4, 11).get_line_to(Point(4, 11)))
