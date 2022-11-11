#!/usr/bin/python3
"""
    define a class 'Square'
"""


class Square:
    """
        square with private instance attribute: 'size'
    """

    def __init__(self, size=0, position=(0, 0)):
    """
       size of the new square
    """
    self.size = size
    self.position = position

    @property
                    def size(self):
                        """
                        shows current size of square
                        """
                        return (self.__size)


