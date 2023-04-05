#!/usr/bin/python3
"""This module defines a real rectangle."""


class Rectangle:
    """Create the Rectangle class."""

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle.

        Args:
            width
            height

        Attribute:
            __width
            __height
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """
        Property getter.

        Args:
            None

        Return:
            self.__height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the width of the rectangle.

        Args="value"

        Attributes="height"
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__height = value

    @property
    def width(self):
        """
        Property getter.

        Returns:
            self.width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the height of the rectangle.

        Args="value"

        Attributes="width"
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__width = value
