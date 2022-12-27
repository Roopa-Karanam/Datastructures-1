#!/usr/bin/env python
"""
# Palindrome approach 2
Used the while loop to compare the first and last elements by incrementing the first index and decrementing
the last index by 1 at every iteration.
Returns "not a palindrome" if any of the comparisons fail
"""

import sys


def fizzbuzz(given_number):
    for i in range(given_number+1):
        if i % 3 == 0 and i % 5 == 0:
            print(" fizzbuzz")
        elif i % 3 == 0:
            print(" fizz")
        elif i % 5 == 0:
            print(" buzz")
        else:
            print(" ", i)


(fizzbuzz(100))
