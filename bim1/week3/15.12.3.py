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

    def slope_from_origin(self):
        """
        Gets the slope of line defined from point to origin
        :return:
        """
        if self.x == 0 and self.y == 0:
            raise Exception("(0,0) does not define a line from origin")
        return self.y / self.x


test(Point(4,10).slope_from_origin() == 2.5)
test(Point(0,0).slope_from_origin())
