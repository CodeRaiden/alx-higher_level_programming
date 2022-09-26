#!/usr/bin/python3
"""
Module contains a function that returns
True if the obj is exactly an instance of the
specified class else False
"""


def is_same_class(obj, a_class):
    """
    function checks for object of a
    specified class
    """
    return (type(obj) == a_class)
