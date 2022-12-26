#!/usr/bin/env python
"""
# Palindrome approach 2
Used the while loop to compare the first and last elements by incrementing the first index and decrementing
the last index by 1 at every iteration.
Returns "not a palindrome" if any of the comparisons fail
"""

import sys
from queue import LifoQueue


def ReverseString(string):
    x = ""
    y=string
    if len(string) <= 0:
        return string
    else:
        # Initializing a stack
        stack = LifoQueue()
        for i in range(len(string)):
            stack.put(y[i])
        for i in range(len(string)):
            x += stack.get()
    return x


if __name__ == '__main__':
    text = sys.argv[1]
    print(ReverseString(text))
