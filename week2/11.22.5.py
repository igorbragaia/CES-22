import sys

def test(did_pass):
    """
    Prints test result
    :param passou: test result
    :return:
    """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def add_vectors(list1, list2):
    """
    Sums two lists through each index
    :param list1: list
    :param list2: list with len equal to list1
    :return: list, where list[i] = list1[i] + list2[i]
    """
    for i in range(len(list1)):
        list1[i] += list2[i]
    return list1

test(add_vectors([1, 1], [1, 1]) == [2, 2])
test(add_vectors([1, 2], [1, 4]) == [2, 6])
test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])