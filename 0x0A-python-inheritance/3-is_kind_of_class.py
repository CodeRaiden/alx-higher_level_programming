#!/usr/bin/python3
"""
Module contains a function that returns True
if the object is an instance of, or if the object
is an instance of a class that inherited from, the
specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    function returns True if obj is
    instance of inherited class
    """
    return (isinstance(obj, a_class))
