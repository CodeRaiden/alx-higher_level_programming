#!/usr/bin/python3
"""
Module contains a class
with public instance and Raises
exception when required
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inherits from rectangle
    """
    def __init__(self, size):
        """
        class instantiation
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
