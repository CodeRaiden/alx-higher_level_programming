#!/usr/bin/python3
"""
This module adds 2 integers a and b and returns the sum.
Function only accepts integers or floats as inputs.
a and b, if float values will be converted to integer.
"""


def add_integer(a, b=98):
    """
    add integer function
    """
    if a isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if b isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
