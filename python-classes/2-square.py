#!/usr/bin/python3
"""
a class square that defines a square , based on '1-square.py'
"""


class Square:
    """
    square has private instance att.: 'size'
    """

    def __init__(self, size=0):
        """
        size of new square is an int.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
