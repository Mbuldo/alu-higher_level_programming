#!/usr/bin/python3
"""
write a class 'square'

"""


class Square:
    """
    square has private instance att.: size

    """

    def __init__(self, size=0):
        """
        define size att.

        """
        self.__size = size

    @property
    def size(self):
        """returns the size att."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """shows current size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """print area of square"""
        square_area = self.__size ** 2
        return square_area

    def my_print(self):
        """print square with char #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
