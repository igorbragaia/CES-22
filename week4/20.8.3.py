from nltk import word_tokenize
from pprint import pprint


map = dict()
with open("alice.txt", "r") as f:
    for line in f:
        for word in word_tokenize(line):
            if word not in map:
                map[word] = 1
            else:
                map[word] += 1


pprint(map)