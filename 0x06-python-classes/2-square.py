#!/usr/bin/python3
"""
This class defines a square with a given size.

    * Private instance attribute: size
    * Instantiation with optional size: def __init__(self, size=0):
    * size must be an integer, otherwise raise a TypeError exception with
      the message size must be an integer
    * if size is less than 0, raise a ValueError exception with the message
      size must be >= 0
    * You are not allowed to import any module
"""


class Square:
    """A class representing a Square."""

    def __init__(self, size=0):
        """
        Initialize a square with a given size.

        @param size: the size of the square (default 0)
        :type size: int
        :raises TypeError: if size is not an integer
        :raises ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
