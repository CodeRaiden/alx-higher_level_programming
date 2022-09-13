#!/usr/bin/python3
'''
Square class that defines a square
Private instance attribute: size
Instantiation with optional size
'''


class Square:
    '''
    Square class with private instance attribute
    '''

    def __init__(self, size=0):
        '''
        size: is the size of the square
        '''

        try:
            if type(size) is not int:
                raise TypeError("size must be an integer")
            elif isdigit(size) < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
