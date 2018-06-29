import sys

def test(did_pass):
    """
    Prints test result
    :param did_pass: test result
    :return:
    """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def scalar_mult(scalar, lista):
    """
    Map a list in which element turns scalar * element
    :param scalar:
    :param lista:
    :return:
    """
    return [scalar * element for element in lista]

test(scalar_mult(5, [1, 2]) == [5, 10])
test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
