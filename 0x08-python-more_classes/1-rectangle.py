#!/usr/bin/python3
"""This module creates, defines attributes of class Rectangle."""


class Rectangle:
    """Creating the class Rectangle.

    Args:
        None

    Attributes:
        None

    Raises:
        TypeError: if the value is not an integer.
        ValueError: if the value is less than 0.
    """

    def __init__(self, width=0, height=0):
        """Instantiate the Rectangle.

        Attributes:
            width:
                the width of the rectangle.
            height:
                the height of the rectangle.
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Get height property.

        Returns:
            __height: to the instance
            # __height is a private instance attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set height to a value."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    @property
    def width(self):
        """Get width property.

        Returns:
            __width to the instance.
            # __width is a private instance attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set width to a value."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value
