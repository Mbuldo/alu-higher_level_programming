#!/bin/usr/python3
"""
create square

"""


class Square:
    """
    square with private instance att.: size

    """

    def __init__(self, size=0):
        """
        size, int.

        """
        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        square_area = self.__size ** 2
        return square_area
