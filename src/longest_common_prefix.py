#!/usr/bin/env python
"""
#Last word is to count the number of characters in the last word
Iterate

"""
import sys


def MinString(list_of_strings):
    minimumLength = len(list_of_strings[0])
    minimum_index = 0
    for i in range(len(list_of_strings)):
        if len(list_of_strings[i]) < minimumLength:
            minimumLength = len(list_of_strings[i])
            minimum_index = i
    return minimum_index


def LongestCommonPrefix(string):
    minimum_index = MinString(string)
    minString = string[minimum_index]
    ans_str = ""
    for i in range(len(minString)):
        for j in range(len(string)):
            if minString[i] != string[j][i]:
                return ans_str
        ans_str += minString[i]
    return ans_str


text = ["abcdefg", "abcd","abcde", "" ]
print(LongestCommonPrefix(text))

# if __name__ == '__main__':
#     # text = sys.argv[1]
#     text = ["abcdefg", "abcde", "abcd", "abc"]
#     print(LongestCommonPrefix(text))
