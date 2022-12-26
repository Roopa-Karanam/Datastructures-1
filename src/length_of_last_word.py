#!/usr/bin/env python
"""
#Last word is to count the number of characters in the last word
Iterate
"""
import sys


def LastWord(string):
    x = len(string)
    length = x - 1
    count = 0
    while string[length] == " " and length >= 0:
        # print(length)
        length = length - 1
    if length > 0:

        while string[length] != " " and length > 0:
            count = count + 1
            length = length - 1
    else:
        return length + 1

    return count


if __name__ == '__main__':
    text = sys.argv[1]
    print(LastWord(text))
