#!/usr/bin/python3
"""This module defines a Square with a given size."""


class Square:
    """
    This class defines a square with a given size.

    Attributes:
        size (int): The size of the square.

    Methods:
        area(): Returns the area of the Square.
    """

    def __init__(self, size=0):
        """
        Initialize a new instance of the Square class.

        Args:
            size (int):  The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Get (or retrieves) the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set (or modify or manipulate) the size of the square.

        Args:
            Value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: the area of the square.
        """
        return self.__size**2
