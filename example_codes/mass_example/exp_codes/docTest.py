#!/usr/bin/env python3
# coding=utf-8
# title          :docTest.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/11/2 17:07
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script


def square(x):
    """
    Squares a number.
    >>> square(2)
    4
    >>> square(4)
    16
    """
    return x*x


if __name__ == '__main__':
    import doctest
    import docTest
    doctest.testfile(docTest)
