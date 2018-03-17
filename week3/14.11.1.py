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


def present_in_both(list1, list2):
    response = []
    for el in list2:
        if el in list1:
            list1.remove(el)
            response.append(el)
    return response


def present_only_in_first(list1, list2):
    for el in list2:
        if el in list1:
            list1.remove(el)
    return list1


def present_only_in_second(list1, list2):
    return present_only_in_first(list2, list1)


def present_either_on_first_or_second(list1, list2):
    #idea: let A, B lists, so then A U B = A + B - A inter B
    response = present_only_in_first(present_only_in_first(list1, list2) + present_only_in_second(list1, list2), present_in_both(list1, list2))
    return sorted(response)


def bagdiff(list1, list2):
    return present_only_in_first(list1, list2)


if __name__ == '__main__':
    test(present_in_both([1, 2, 2, 3, 4], [1, 2]) == [1, 2])
    test(present_in_both([1, 1, 2, 2, 3, 4], [1, 1, 1]) == [1, 1])
    test(present_in_both([1, 2, 2, 3, 4], []) == [])
    test(present_in_both([], []) == [])

    test(present_only_in_first([1, 2, 2, 3, 4], [1, 3]) == [2, 2, 4])
    test(present_only_in_first([1, 2, 2, 3, 4], [1]) == [2, 2, 3, 4])
    test(present_only_in_first([1, 2, 2, 3, 4], []) == [1, 2, 2, 3, 4])
    test(present_only_in_first([], []) == [])

    test(present_only_in_second([1, 2, 2, 3, 3, 4], [1, 3]) == [])
    test(present_only_in_second([1, 2, 2, 3, 4], [1, 1, 5]) == [1, 5])
    test(present_only_in_second([1, 2, 2, 3, 4], []) == [])
    test(present_only_in_second([], []) == [])

    test(present_either_on_first_or_second([1, 2, 2, 3, 4], [1, 1, 3]) == [1, 1, 2, 2, 3, 4])
    test(present_either_on_first_or_second([1, 2, 2, 3, 4], [1]) == [1, 2, 2, 3, 4])
    test(present_either_on_first_or_second([1, 2, 2, 3, 4], []) == [1, 2, 2, 3, 4])
    test(present_either_on_first_or_second([], []) == [])

    test(bagdiff([5, 7, 11, 11, 11, 12, 13], [7, 8, 11]) == [5, 11, 11, 12, 13])
    test(bagdiff([1, 2, 2, 3, 4], [2, 3]) == [1, 2, 4])
    test(bagdiff([1, 2, 2, 3, 4], [1]) == [2, 2, 3, 4])
    test(bagdiff([1, 2, 2, 3, 4], []) == [1, 2, 2, 3, 4])
    test(bagdiff([], []) == [])
