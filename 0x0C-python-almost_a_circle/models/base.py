#!/usr/bin/python3
"""
The base class
"""


class Base:
    """
    This class contains a private attribute and a class
    constructor definition to check for id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
