#!/usr/bin/env python
"""
# Reverse the string
 used range to get numbers in reverse order from the length of the give string to zero and taken the
 corresponding character to add it into a new list and returned tha list.
"""
import sys


def ReverseString(string):
    x = ""
    if len(string) <= 1:
        return string
    else:
        y = string
        for i in range(len(string) - 1, -1, -1):
            x += (y[i])
    return x


if __name__ == '__main__':

    try:
        text = sys.argv[1]
        print(ReverseString(text))
    except ValueError:
        text = "gnirts dilav edivorp esaelP"
        print(ReverseString(text))
    finally:
        print("Thanks for using the String Reverse services")
