#!/usr/bin/env python
"""
# Reverse the string
The technique used here is to swap the first and
the last elements of the string. End swapping when first is greater than last
"""
import sys


def Swap(x, y, string):
    m = list(string)
    temp = m[x]
    m[x] = m[y]
    m[y] = temp
    m = "".join(m)
    return m


def ReverseString2(string):
    if len(string) <= 1:
        return string
    start = 0
    end = len(string) - 1
    m = string
    while start < end:
        print("I am inside while")
        m= Swap(start, end, m)
        print(m[start], "and", m[end])
        start += 1
        end -= 1
        print(m)
        print("start is", start)
        print("end is ", end)

    return m


if __name__ == '__main__':
    text = sys.argv[1]
    print(ReverseString2(text))
