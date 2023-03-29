#!/usr/bin/python3
"""This module defines a square with a given size."""


class Square:
    """A class representing a Square."""

    def __init__(self, size=0):
        """
        Initialize a square.

        @param size:
                    the size of the square (default 0)

        :type size:
                    int

        :raises TypeError:
                          if size is not an integer

        :raises ValueError:
                           if size is less than 0

        Returns:
                the current square area

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        return self.__size**2
