#!/usr/bin/python3
"""
create square

"""


class Square:
    """
    create square with private instance att.: size

    """

    def __init__(self, size=0):
        """
      a square with a private instance att.: size  

        """
        self.size = size

    @property
    def size(self):
        """shows current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """must proof size to be an integer
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return: area of the square

        """
        return (self.__size * self.__size)
