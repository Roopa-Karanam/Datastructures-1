#!/usr/bin/env python
"""
# Palindrome approach 2
Used the while loop to compare the first and last elements by incrementing the first index and decrementing
the last index by 1 at every iteration.
Returns "not a palindrome" if any of the comparisons fail
"""

import sys


def isPalindrome(given_string):
    """

    :param given_string: String for evaluating if palindrome
    :return: boolean (True for palindrome false for not palindrome)
    """
    if len(given_string) <= 1:
        return True
    given_string = given_string.lower()
    first = 0
    last = len(given_string) - 1
    while first < last:
        if given_string[first] == given_string[last]:
            last = last - 1
            first = first + 1
        else:
            return False

    return True


if __name__ == '__main__':
    text = sys.argv[1]
    print(isPalindrome(text))
