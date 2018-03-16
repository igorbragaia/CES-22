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


def cleanword(string):
    return "".join([x for x in string if (x >='a' and x <= 'z') or (x >= 'A' and x <= 'Z')])


def has_dashdash(string):
    return '--' in string


def extract_words(string):
    return [word.lower() for word in "".join([x if (x >='a' and x <= 'z') or (x >= 'A' and x <= 'Z') else ' ' for x in string]).split(' ') if word != '']


def wordcount(string, lista):
    return sum([1 if element == string else 0 for element in lista])


def wordset(lista):
    return sorted(set(lista))


def longestword(lista):
    return max([len(string) for string in lista]) if lista != [] else 0


if __name__ == '__main__':
    test(cleanword("what?") == "what")
    test(cleanword("'now!'") == "now")
    test(cleanword("?+='w-o-r-d!,@$()'") == "word")

    test(has_dashdash("distance--but"))
    test(not has_dashdash("several"))
    test(has_dashdash("spoke--"))
    test(has_dashdash("distance--but"))
    test(not has_dashdash("-yo-yo-"))

    test(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
         ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now'])
    test(extract_words("she tried to curtsey as she spoke--fancy") ==
         ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy'])

    test(wordcount("now", ["now", "is", "time", "is", "now", "is", "is"]) == 2)
    test(wordcount("is", ["now", "is", "time", "is", "now", "the", "is"]) == 3)
    test(wordcount("time", ["now", "is", "time", "is", "now", "is", "is"]) == 1)
    test(wordcount("frog", ["now", "is", "time", "is", "now", "is", "is"]) == 0)

    test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
         ["is", "now", "time"])
    test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
         ["I", "a", "am", "is"])
    test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
         ["a", "am", "are", "be", "but", "is", "or"])

    test(longestword(["a", "apple", "pear", "grape"]) == 5)
    test(longestword(["a", "am", "I", "be"]) == 2)
    test(longestword(["this", "supercalifragilisticexpialidocious"]) == 34)
    test(longestword([]) == 0)
