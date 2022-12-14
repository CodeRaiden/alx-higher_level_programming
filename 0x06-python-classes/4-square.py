#!/usr/bin/python3
"""
Square class definition
"""


class Square:
    """
    Square class with private instance attribute size
    """

    def __init__(self, size=0):
        """
        Args:
            size: size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """
    getter wrapper to retrieve the size property
    """

    @property
    def size(self):
        return self.__size
    """
    setter wrapper to set the size property
    """

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        """
        Returns area of the square instance
        """

    def area(self):
        return self.__size * self.__size
