#!/usr/bin/python3
"""
The class Rectangle that inherits from Base
"""
from model.Base import Base


class Rectangle(Base):
    """
    Class Rectangle inherits from Base
    Private instance attributes, each with its own public getter and setter
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        instaniation of the class private intances
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    """
    Returns width value
    """
    def width(self, value):
        return self.__width = value

    @width.setter
    """
    Validates that an int value greater than 0 is set for the width
    """
    def width(self, value):
        if value is not int
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        elif value.isdigit():
            __self.width = value

    @property
    """
    Returns height value
    """
    def height(self, value):
        return self.__height = value

    @height.setter
    """
    Validates that an int value greater than 0 is set for the height
    """
    def height(self, value):
        if value is not int
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        elif value.isdigit():
            __self.height = value

    @property
    """
    Returns x value
    """
    def x(self, value):
        return self.__x = value

    @x.setter
    """
    Validates that an int value greater than 0 is set for x
    """
    def x(self, value):
        if value is not int
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        elif value.isdigit():
            __self.x = value

    @property
    """
    Returns y value
    """
    def y(self, value):
        return self.__y = value

    @y.setter
    """
    Validates that an int value greater than 0 is set for y
    """
    def y(self, value):
        if value is not int
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        elif value.isdigit():
            __self.y = value

    def area(self):
        """
        Method calculates the area of a rectangle
        """
        return (__self.width * __self.height)

    def display(self):
        """
        Method prints in stdout the Rectangle
        instance with the character #
        """
        print(("\n" * self.__y) +
              "\n".join(((" " * self.__x) + ("#" * self.__width))
                        for i in range(self.__height)))

    def __str__(self):
        """
        Update the class Rectangle by overriding the __str__ method
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id, __self.x, __self.y, __self.width, __self.height)

    def update(self, *args):
        """
        Method updates the class Rectangle by adding
        the public method that assigns an argument to
        each attribute
        """
        def update(self, *args, **kwargs):
        """updates multiple attributes"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """dictionary representation of a Rectangle"""
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
            
