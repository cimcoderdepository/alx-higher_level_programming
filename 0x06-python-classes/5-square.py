#!/usr/bin/python3
"""This module represents a square."""


class Square:
    """
    A class to represent a square.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size=0): Constructs a new Square object.
        area(self): Calculates the area of the square.
        my_print(self): Prints the square to the console.
    """

    def __init__(self, size=0):
        """
        Construct a new Square object.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size**2

    def my_print(self):
        """Print the square to the console."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
