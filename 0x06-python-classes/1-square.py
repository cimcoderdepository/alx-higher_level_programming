#!/usr/bin/python3
class Square:
    """A class representing a square."""

    def __init__(self, size):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.

        Attributes:
            __size (int): The size of the square.
        """
        self.__size = size
        # Note that __size (double leading undercore) is a private instance
        # attribute, indicated by the double underscores before its name.
        # This means that it can only be accessed from within the class and
        # not from outside of it. The size argument passed to the constructor
        # is assigned to this attribute.
